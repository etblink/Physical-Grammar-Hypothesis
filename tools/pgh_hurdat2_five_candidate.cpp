#include <algorithm>
#include <array>
#include <bit>
#include <cassert>
#include <cctype>
#include <cmath>
#include <cstdint>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <limits>
#include <map>
#include <numeric>
#include <optional>
#include <set>
#include <sstream>
#include <stdexcept>
#include <string>
#include <string_view>
#include <tuple>
#include <utility>
#include <vector>

namespace pgh {

constexpr int K = 9;
constexpr int STATES = K*K*K;
constexpr int CAL1_REPS = 4999;
constexpr int CAL2_REPS = 1999;
const std::array<std::string, K> STATUS = {"TD","TS","HU","EX","SD","SS","LO","WV","DB"};

static std::string trim(std::string s) {
    auto notsp=[](unsigned char c){return !std::isspace(c);};
    s.erase(s.begin(), std::find_if(s.begin(), s.end(), notsp));
    s.erase(std::find_if(s.rbegin(), s.rend(), notsp).base(), s.end());
    return s;
}
static std::vector<std::string> split_csv(const std::string& line) {
    std::vector<std::string> out; std::string cur; std::stringstream ss(line);
    while (std::getline(ss, cur, ',')) out.push_back(trim(cur));
    if (!line.empty() && line.back()==',') out.emplace_back("");
    return out;
}
static bool all_digits(std::string_view s) {
    return !s.empty() && std::all_of(s.begin(), s.end(), [](unsigned char c){return std::isdigit(c);});
}
static int status_id(const std::string& s) {
    for(int i=0;i<K;++i) if(s==STATUS[i]) return i;
    return -1;
}
static int state_id(int a,int b,int c){return (a*K+b)*K+c;}
static std::array<int,3> state_tuple(int x){return {x/(K*K),(x/K)%K,x%K};}

static int64_t days_from_civil(int y, unsigned m, unsigned d) {
    y -= m <= 2;
    const int era = (y >= 0 ? y : y-399) / 400;
    const unsigned yoe = static_cast<unsigned>(y - era * 400);
    const unsigned doy = (153*(m + (m > 2 ? static_cast<unsigned>(-3) : 9)) + 2)/5 + d-1;
    const unsigned doe = yoe * 365 + yoe/4 - yoe/100 + doy;
    return static_cast<int64_t>(era) * 146097 + static_cast<int64_t>(doe);
}
static bool leap(int y){ return y%4==0 && (y%100!=0 || y%400==0); }
static bool valid_date(int y,int m,int d){
    if(m<1||m>12||d<1) return false;
    static const int md[]={31,28,31,30,31,30,31,31,30,31,30,31};
    int lim=md[m-1]+(m==2&&leap(y)); return d<=lim;
}
static int64_t stamp_hours(const std::string& date, const std::string& time) {
    if(date.size()!=8 || !all_digits(date) || time.size()!=4 || !all_digits(time)) throw std::runtime_error("malformed date/time");
    int y=std::stoi(date.substr(0,4)), m=std::stoi(date.substr(4,2)), d=std::stoi(date.substr(6,2));
    int hh=std::stoi(time.substr(0,2)), mm=std::stoi(time.substr(2,2));
    if(!valid_date(y,m,d)||hh<0||hh>23||mm<0||mm>59) throw std::runtime_error("invalid date/time");
    return days_from_civil(y,static_cast<unsigned>(m),static_cast<unsigned>(d))*24 + hh;
}

struct Triple { uint8_t a,b,c; };
struct ParseAudit {
    size_t storms=0, raw_records=0, in_range_records=0, standard_records=0;
    size_t recognized_records=0, unrecognized_status_breaks=0, continuity_breaks=0;
    size_t runs=0, retained_triples=0, trailing_records_discarded=0;
};
struct ParsedData {
    std::vector<Triple> triples;
    std::vector<std::vector<int>> block_runs;
    ParseAudit audit;
};

static bool standard_time(const std::string& t){return t=="0000"||t=="0600"||t=="1200"||t=="1800";}

static ParsedData parse_hurdat(std::istream& in) {
    ParsedData out;
    std::string line;
    bool have_storm=false;
    int declared=0, seen=0;
    std::vector<std::pair<int64_t,int>> current_run;
    int64_t last_standard = std::numeric_limits<int64_t>::min();

    auto flush_run=[&](){
        if(current_run.empty()) return;
        out.audit.runs++;
        std::vector<int> br;
        size_t ntrip=current_run.size()/3;
        for(size_t i=0;i<ntrip;++i){
            int a=current_run[3*i].second,b=current_run[3*i+1].second,c=current_run[3*i+2].second;
            out.triples.push_back(Triple{static_cast<uint8_t>(a),static_cast<uint8_t>(b),static_cast<uint8_t>(c)});
            br.push_back(state_id(a,b,c));
        }
        out.audit.retained_triples += ntrip;
        out.audit.trailing_records_discarded += current_run.size()%3;
        if(!br.empty()) out.block_runs.push_back(std::move(br));
        current_run.clear();
    };
    auto finish_storm=[&](){
        if(!have_storm) return;
        flush_run();
        if(seen!=declared) throw std::runtime_error("declared HURDAT2 record count mismatch");
        have_storm=false;
    };

    while(std::getline(in,line)){
        if(!line.empty() && line.back()=='\r') line.pop_back();
        if(trim(line).empty()) continue;
        auto f=split_csv(line);
        bool header = f.size()>=3 && f[0].size()==8 && f[0].rfind("AL",0)==0 && all_digits(std::string_view(f[0]).substr(2));
        if(header){
            finish_storm();
            if(!all_digits(f[2])) throw std::runtime_error("malformed HURDAT2 header count");
            declared=std::stoi(f[2]); if(declared<0) throw std::runtime_error("negative record count");
            seen=0; have_storm=true; last_standard=std::numeric_limits<int64_t>::min(); out.audit.storms++;
            continue;
        }
        if(!have_storm) throw std::runtime_error("data record before Atlantic HURDAT2 header");
        if(f.size()<4) throw std::runtime_error("malformed HURDAT2 record");
        seen++; out.audit.raw_records++;
        const std::string& date=f[0]; const std::string& time=f[1];
        int64_t ts=stamp_hours(date,time);
        int year=std::stoi(date.substr(0,4));
        if(year<1988 || year>2025) continue;
        out.audit.in_range_records++;
        if(!standard_time(time)) continue;
        out.audit.standard_records++;
        if(last_standard!=std::numeric_limits<int64_t>::min() && ts<=last_standard) throw std::runtime_error("duplicate or non-increasing standard timestamp within storm");
        if(last_standard!=std::numeric_limits<int64_t>::min() && ts-last_standard!=6){ flush_run(); out.audit.continuity_breaks++; }
        last_standard=ts;
        int sid=status_id(f[3]);
        if(sid<0){ flush_run(); out.audit.unrecognized_status_breaks++; continue; }
        out.audit.recognized_records++;
        current_run.emplace_back(ts,sid);
    }
    finish_storm();
    return out;
}

static long double clamp_g2(long double x){
    if(x<0 && x>-1e-9L) return 0;
    if(x<=-1e-9L || !std::isfinite(x)) throw std::runtime_error("invalid G2 numeric result");
    return x;
}
static long double g2_uncond(const std::vector<Triple>& t, int xrole, int yrole){
    long double nxy[K][K]{}; long double nx[K]{}, ny[K]{}; long double N=static_cast<long double>(t.size());
    auto get=[](const Triple& z,int r)->int{return r==0?z.a:(r==1?z.b:z.c);};
    for(auto &z:t){int x=get(z,xrole),y=get(z,yrole); nxy[x][y]++;nx[x]++;ny[y]++;}
    long double g=0; if(N==0) return 0;
    for(int x=0;x<K;++x) for(int y=0;y<K;++y) if(nxy[x][y]>0)
        g += 2*nxy[x][y]*std::log((nxy[x][y]*N)/(nx[x]*ny[y]));
    return clamp_g2(g);
}
static long double g2_cond(const std::vector<Triple>& t, int xrole,int yrole,int zrole){
    long double nxyz[K][K][K]{}; long double nxz[K][K]{},nyz[K][K]{},nz[K]{};
    auto get=[](const Triple& q,int r)->int{return r==0?q.a:(r==1?q.b:q.c);};
    for(auto&q:t){int x=get(q,xrole),y=get(q,yrole),z=get(q,zrole);nxyz[x][y][z]++;nxz[x][z]++;nyz[y][z]++;nz[z]++;}
    long double g=0;
    for(int x=0;x<K;++x)for(int y=0;y<K;++y)for(int z=0;z<K;++z) if(nxyz[x][y][z]>0)
        g += 2*nxyz[x][y][z]*std::log((nxyz[x][y][z]*nz[z])/(nxz[x][z]*nyz[y][z]));
    return clamp_g2(g);
}
static long double stat_h(const std::vector<Triple>& t,int h){
    switch(h){case 1:return g2_uncond(t,0,2);case 2:return g2_cond(t,0,1,2);case 3:return g2_uncond(t,0,1);case 4:return g2_cond(t,1,2,0);case 5:return g2_uncond(t,1,2);default:throw std::runtime_error("bad h");}
}

struct Xoshiro {
    std::array<uint64_t,4> s{};
    static uint64_t rotl(uint64_t x,int k){return (x<<k)|(x>>(64-k));}
    uint64_t next(){
        uint64_t result=rotl(s[1]*5ULL,7)*9ULL;
        uint64_t t=s[1]<<17;
        s[2]^=s[0]; s[3]^=s[1]; s[1]^=s[2]; s[0]^=s[3]; s[2]^=t; s[3]=rotl(s[3],45);
        return result;
    }
    uint64_t bounded(uint64_t n){
        if(n==0) throw std::runtime_error("bounded zero");
        uint64_t threshold = static_cast<uint64_t>(-n) % n;
        for(;;){uint64_t r=next(); if(r>=threshold) return r%n;}
    }
};
static uint64_t splitmix64(uint64_t &x){
    uint64_t z=(x+=0x9E3779B97F4A7C15ULL); z=(z^(z>>30))*0xBF58476D1CE4E5B9ULL; z=(z^(z>>27))*0x94D049BB133111EBULL; return z^(z>>31);
}
static Xoshiro stream_from_master(const std::array<uint64_t,4>& m,int cal,int h,uint64_t r){
    uint64_t x=m[0]^Xoshiro::rotl(m[1],13)^Xoshiro::rotl(m[2],29)^Xoshiro::rotl(m[3],47)
        ^(0x9E3779B97F4A7C15ULL*static_cast<uint64_t>(cal))
        ^(0xD1B54A32D192ED03ULL*static_cast<uint64_t>(h))
        ^(0x94D049BB133111EBULL*(r+1));
    Xoshiro g; for(int i=0;i<4;++i)g.s[i]=splitmix64(x); if((g.s[0]|g.s[1]|g.s[2]|g.s[3])==0)g.s[3]=1; return g;
}
static std::array<uint64_t,4> parse_master_hex(const std::string& hex){
    if(hex.size()!=64) throw std::runtime_error("master seed must be 64 lowercase hex");
    for(char c:hex) if(!((c>='0'&&c<='9')||(c>='a'&&c<='f'))) throw std::runtime_error("master seed must be lowercase hex");
    std::array<uint64_t,4> m{};
    for(int w=0;w<4;++w){uint64_t x=0;for(int j=0;j<16;++j){char c=hex[w*16+j];int v=c<='9'?c-'0':c-'a'+10;x=(x<<4)|static_cast<uint64_t>(v);}m[w]=x;}
    return m;
}

template<class T> static void fisher_yates(std::vector<T>& v,Xoshiro& g){for(size_t i=v.size();i>1;--i){size_t j=static_cast<size_t>(g.bounded(i));std::swap(v[i-1],v[j]);}}
static bool exceed(long double rep,long double obs){return rep + 1e-12L*std::max(1.0L,std::fabs(obs)) >= obs;}

struct Counts {
    std::array<uint64_t,STATES> n{}, w{};
    std::array<uint64_t,K> WA{},WB{},WC{};
    std::array<uint64_t,K*K> WAB{},WAC{},WBC{};
    uint64_t W=0,N=0;
};
static Counts make_counts(const std::vector<Triple>& tr){
    Counts c; c.N=tr.size(); for(auto&t:tr)c.n[state_id(t.a,t.b,t.c)]++;
    for(int x=0;x<STATES;++x){c.w[x]=2*c.n[x]+1;c.W+=c.w[x];auto q=state_tuple(x);int a=q[0],b=q[1],d=q[2];c.WA[a]+=c.w[x];c.WB[b]+=c.w[x];c.WC[d]+=c.w[x];c.WAB[a*K+b]+=c.w[x];c.WAC[a*K+d]+=c.w[x];c.WBC[b*K+d]+=c.w[x];}
    return c;
}
struct BigUInt {
    std::vector<uint32_t> w;
    BigUInt() = default;
    explicit BigUInt(uint64_t x){
        uint32_t lo=static_cast<uint32_t>(x & 0xffffffffULL);
        uint32_t hi=static_cast<uint32_t>(x >> 32);
        if(lo || hi) w.push_back(lo);
        if(hi) w.push_back(hi);
    }
    void norm(){ while(!w.empty() && w.back()==0) w.pop_back(); }
    bool zero() const { return w.empty(); }
    static int cmp(const BigUInt&a,const BigUInt&b){
        if(a.w.size()!=b.w.size()) return a.w.size()<b.w.size()?-1:1;
        for(size_t i=a.w.size();i>0;--i) if(a.w[i-1]!=b.w[i-1]) return a.w[i-1]<b.w[i-1]?-1:1;
        return 0;
    }
    static BigUInt add(const BigUInt&a,const BigUInt&b){
        BigUInt r; size_t n=std::max(a.w.size(),b.w.size()); r.w.resize(n,0); uint64_t carry=0;
        for(size_t i=0;i<n;++i){ uint64_t av=i<a.w.size()?a.w[i]:0, bv=i<b.w.size()?b.w[i]:0; uint64_t cur=av+bv+carry; r.w[i]=static_cast<uint32_t>(cur); carry=cur>>32; }
        if(carry) r.w.push_back(static_cast<uint32_t>(carry));
        return r;
    }
    static BigUInt mul(const BigUInt&a,const BigUInt&b){
        BigUInt r; if(a.zero()||b.zero()) return r; r.w.assign(a.w.size()+b.w.size(),0);
        for(size_t i=0;i<a.w.size();++i){
            uint64_t carry=0;
            for(size_t j=0;j<b.w.size();++j){
                uint64_t cur=static_cast<uint64_t>(a.w[i])*static_cast<uint64_t>(b.w[j]) + static_cast<uint64_t>(r.w[i+j]) + carry;
                r.w[i+j]=static_cast<uint32_t>(cur); carry=cur>>32;
            }
            size_t k=i+b.w.size();
            while(carry){
                if(k==r.w.size()) r.w.push_back(0);
                uint64_t cur=static_cast<uint64_t>(r.w[k])+carry; r.w[k]=static_cast<uint32_t>(cur); carry=cur>>32; ++k;
            }
        }
        r.norm(); return r;
    }
    void dec1(){
        if(zero()) throw std::runtime_error("BigUInt underflow");
        size_t i=0; while(i<w.size() && w[i]==0){w[i]=0xffffffffU;++i;} if(i==w.size()) throw std::runtime_error("BigUInt underflow"); --w[i]; norm();
    }
    unsigned bit_length() const { if(zero()) return 0; uint32_t h=w.back(); return static_cast<unsigned>((w.size()-1)*32 + (32-std::countl_zero(h))); }
};
static BigUInt big_product64(std::initializer_list<uint64_t> xs){ BigUInt r(uint64_t(1)); for(uint64_t x:xs) r=BigUInt::mul(r,BigUInt(x)); return r; }
static BigUInt big_product(std::initializer_list<BigUInt> xs){ BigUInt r(uint64_t(1)); for(const auto&x:xs) r=BigUInt::mul(r,x); return r; }

struct Rat { BigUInt n,d; };
static Rat qrat(const Counts& c,int h,int sid){
    auto q=state_tuple(sid);int a=q[0],b=q[1],z=q[2];
    switch(h){
        case 1:return {big_product64({c.WA[a],c.WC[z],c.w[sid]}),big_product64({c.W,c.W,c.WAC[a*K+z]})};
        case 2:return {big_product64({c.WAC[a*K+z],c.WBC[b*K+z]}),big_product64({c.W,c.WC[z]})};
        case 3:return {big_product64({c.WA[a],c.WB[b],c.w[sid]}),big_product64({c.W,c.W,c.WAB[a*K+b]})};
        case 4:return {big_product64({c.WAB[a*K+b],c.WAC[a*K+z]}),big_product64({c.W,c.WA[a]})};
        case 5:return {big_product64({c.WB[b],c.WC[z],c.w[sid]}),big_product64({c.W,c.W,c.WBC[b*K+z]})};
        default:throw std::runtime_error("bad h");
    }
}
static bool exact_q_factorization_checks(const Counts& c,int h){
    auto sum9=[](const std::array<uint64_t,K>& a){uint64_t s=0;for(auto x:a)s+=x;return s;};
    if(sum9(c.WA)!=c.W || sum9(c.WB)!=c.W || sum9(c.WC)!=c.W) return false;
    if(h==1){ for(int a=0;a<K;++a)for(int z=0;z<K;++z){uint64_t q=0;for(int b=0;b<K;++b)q+=c.w[state_id(a,b,z)];if(q!=c.WAC[a*K+z])return false;} return true; }
    if(h==2){ for(int z=0;z<K;++z){uint64_t sa=0,sb=0;for(int a=0;a<K;++a)sa+=c.WAC[a*K+z];for(int b=0;b<K;++b)sb+=c.WBC[b*K+z];if(sa!=c.WC[z]||sb!=c.WC[z])return false;} return true; }
    if(h==3){ for(int a=0;a<K;++a)for(int b=0;b<K;++b){uint64_t q=0;for(int z=0;z<K;++z)q+=c.w[state_id(a,b,z)];if(q!=c.WAB[a*K+b])return false;} return true; }
    if(h==4){ for(int a=0;a<K;++a){uint64_t sb=0,sz=0;for(int b=0;b<K;++b)sb+=c.WAB[a*K+b];for(int z=0;z<K;++z)sz+=c.WAC[a*K+z];if(sb!=c.WA[a]||sz!=c.WA[a])return false;} return true; }
    if(h==5){ for(int b=0;b<K;++b)for(int z=0;z<K;++z){uint64_t q=0;for(int a=0;a<K;++a)q+=c.w[state_id(a,b,z)];if(q!=c.WBC[b*K+z])return false;} return true; }
    return false;
}
static int sample_weights(const uint64_t* w,int n,Xoshiro& g){uint64_t total=0;for(int i=0;i<n;++i)total+=w[i];uint64_t r=g.bounded(total),cum=0;for(int i=0;i<n;++i){cum+=w[i];if(r<cum)return i;}throw std::runtime_error("sample weights");}
static int sample_q(const Counts& c,int h,Xoshiro& g){
    int a,b,z;
    switch(h){
        case 1:{a=sample_weights(c.WA.data(),K,g);z=sample_weights(c.WC.data(),K,g);uint64_t ww[K];for(int j=0;j<K;++j)ww[j]=c.w[state_id(a,j,z)];b=sample_weights(ww,K,g);break;}
        case 2:{z=sample_weights(c.WC.data(),K,g);uint64_t aa[K],bb[K];for(int i=0;i<K;++i){aa[i]=c.WAC[i*K+z];bb[i]=c.WBC[i*K+z];}a=sample_weights(aa,K,g);b=sample_weights(bb,K,g);break;}
        case 3:{a=sample_weights(c.WA.data(),K,g);b=sample_weights(c.WB.data(),K,g);uint64_t zz[K];for(int i=0;i<K;++i)zz[i]=c.w[state_id(a,b,i)];z=sample_weights(zz,K,g);break;}
        case 4:{a=sample_weights(c.WA.data(),K,g);uint64_t bb[K],zz[K];for(int i=0;i<K;++i){bb[i]=c.WAB[a*K+i];zz[i]=c.WAC[a*K+i];}b=sample_weights(bb,K,g);z=sample_weights(zz,K,g);break;}
        case 5:{b=sample_weights(c.WB.data(),K,g);z=sample_weights(c.WC.data(),K,g);uint64_t aa[K];for(int i=0;i<K;++i)aa[i]=c.w[state_id(i,b,z)];a=sample_weights(aa,K,g);break;}
        default:throw std::runtime_error("bad h");
    }
    return state_id(a,b,z);
}

struct Transition {
    std::array<std::map<int,uint64_t>,STATES> t;
    std::array<uint64_t,STATES> T{};
};
static Transition make_transition(const ParsedData& p){Transition z;for(auto&run:p.block_runs)for(size_t i=1;i<run.size();++i){z.t[run[i-1]][run[i]]++;z.T[run[i-1]]++;}return z;}
static Rat proposal_prob(const Counts& c,const Transition& tr,int h,int from,int to){
    Rat q=qrat(c,h,to); uint64_t tc=tr.t[from].count(to)?tr.t[from].at(to):0;
    BigUInt n=BigUInt::add(BigUInt::mul(BigUInt(tc),q.d),q.n);
    BigUInt d=BigUInt::mul(q.d,BigUInt(tr.T[from]+1));
    return {n,d};
}
static int sample_proposal(const Counts& c,const Transition& tr,int h,int from,Xoshiro& g){uint64_t T=tr.T[from];uint64_t r=g.bounded(T+1);if(r==T)return sample_q(c,h,g);uint64_t cum=0;for(auto&[to,n]:tr.t[from]){cum+=n;if(r<cum)return to;}throw std::runtime_error("proposal cumulative");}
static BigUInt uniform_big(const BigUInt& D,Xoshiro& g){
    if(D.zero()) throw std::runtime_error("uniform_big D=0");
    if(D.w.size()==1 && D.w[0]==1) return BigUInt();
    BigUInt dm1=D; dm1.dec1(); unsigned k=dm1.bit_length(); size_t words64=(k+63)/64;
    for(;;){
        BigUInt x; x.w.assign(words64*2,0);
        for(size_t j=0;j<words64;++j){uint64_t r=g.next();x.w[2*j]=static_cast<uint32_t>(r);x.w[2*j+1]=static_cast<uint32_t>(r>>32);}
        if(k%32) x.w[(k-1)/32] &= (uint32_t(1)<<(k%32))-1U;
        size_t keep=(k+31)/32; if(x.w.size()>keep)x.w.resize(keep); x.norm();
        if(BigUInt::cmp(x,D)<0) return x;
    }
}
static bool mh_accept(const Counts& c,const Transition& tr,int h,int x,int y,Xoshiro& g){
    Rat qx=qrat(c,h,x),qy=qrat(c,h,y), rxy=proposal_prob(c,tr,h,x,y), ryx=proposal_prob(c,tr,h,y,x);
    BigUInt num=big_product({qy.n,ryx.n,qx.d,rxy.d});
    BigUInt den=big_product({qy.d,ryx.d,qx.n,rxy.n});
    if(BigUInt::cmp(num,den)>=0) return true;
    return BigUInt::cmp(uniform_big(den,g),num)<0;
}

static std::vector<Triple> permute_h(const std::vector<Triple>& src,int h,Xoshiro& g){
    auto out=src;
    if(h==1||h==5){std::vector<uint8_t> v;v.reserve(out.size());for(auto&t:out)v.push_back(t.c);fisher_yates(v,g);for(size_t i=0;i<out.size();++i)out[i].c=v[i];}
    else if(h==3){std::vector<uint8_t> v;v.reserve(out.size());for(auto&t:out)v.push_back(t.b);fisher_yates(v,g);for(size_t i=0;i<out.size();++i)out[i].b=v[i];}
    else if(h==2){for(int z=0;z<K;++z){std::vector<size_t> idx;std::vector<uint8_t> v;for(size_t i=0;i<out.size();++i)if(out[i].c==z){idx.push_back(i);v.push_back(out[i].b);}fisher_yates(v,g);for(size_t j=0;j<idx.size();++j)out[idx[j]].b=v[j];}}
    else if(h==4){for(int a=0;a<K;++a){std::vector<size_t> idx;std::vector<uint8_t> v;for(size_t i=0;i<out.size();++i)if(out[i].a==a){idx.push_back(i);v.push_back(out[i].c);}fisher_yates(v,g);for(size_t j=0;j<idx.size();++j)out[idx[j]].c=v[j];}}
    else throw std::runtime_error("bad h");
    return out;
}
static std::vector<Triple> bootstrap_h(const ParsedData& p,const Counts& c,const Transition& tr,int h,Xoshiro& g){
    std::vector<Triple> out; out.reserve(p.triples.size());
    for(auto&run:p.block_runs){if(run.empty())continue;int cur=sample_q(c,h,g);auto q=state_tuple(cur);out.push_back(Triple{(uint8_t)q[0],(uint8_t)q[1],(uint8_t)q[2]});for(size_t i=1;i<run.size();++i){int y=sample_proposal(c,tr,h,cur,g);if(mh_accept(c,tr,h,cur,y,g))cur=y;auto r=state_tuple(cur);out.push_back(Triple{(uint8_t)r[0],(uint8_t)r[1],(uint8_t)r[2]});}}
    return out;
}

struct CalResult {std::array<int,5> exceed{}; std::array<bool,5> reject{};};
static std::array<bool,5> holm(const std::array<int,5>& exceed,int reps){
    std::array<int,5> ord={0,1,2,3,4};
    std::sort(ord.begin(),ord.end(),[&](int i,int j){int ai=exceed[i]+1,aj=exceed[j]+1;if(ai!=aj)return ai<aj;return i<j;});
    std::array<bool,5> rej{}; bool stopped=false;
    for(int rank=0;rank<5;++rank){int i=ord[rank],d=5-rank;bool pass=(uint64_t(100)*static_cast<uint64_t>(d)*static_cast<uint64_t>(exceed[i]+1) <= static_cast<uint64_t>(reps+1));if(stopped||!pass){stopped=true;rej[i]=false;}else rej[i]=true;}
    return rej;
}
static CalResult run_cal1(const ParsedData& p,const std::array<uint64_t,4>& m,int reps){CalResult z;std::array<long double,5> obs;for(int h=1;h<=5;++h)obs[h-1]=stat_h(p.triples,h);for(int h=1;h<=5;++h)for(int r=0;r<reps;++r){auto g=stream_from_master(m,1,h,r);auto x=permute_h(p.triples,h,g);if(exceed(stat_h(x,h),obs[h-1]))z.exceed[h-1]++;}z.reject=holm(z.exceed,reps);return z;}
static CalResult run_cal2(const ParsedData& p,const std::array<uint64_t,4>& m,int reps){CalResult z;auto c=make_counts(p.triples);auto tr=make_transition(p);std::array<long double,5> obs;for(int h=1;h<=5;++h)obs[h-1]=stat_h(p.triples,h);for(int h=1;h<=5;++h)for(int r=0;r<reps;++r){auto g=stream_from_master(m,2,h,r);auto x=bootstrap_h(p,c,tr,h,g);if(exceed(stat_h(x,h),obs[h-1]))z.exceed[h-1]++;}z.reject=holm(z.exceed,reps);return z;}

static void support_gate(const ParsedData& p){if(p.triples.size()<1000)throw std::runtime_error("INCONCLUSIVE_DATA_SUPPORT: fewer than 1000 retained triples");for(int role=0;role<3;++role){std::set<int>s;for(auto&t:p.triples)s.insert(role==0?t.a:(role==1?t.b:t.c));if(s.size()<2)throw std::runtime_error("INCONCLUSIVE_DATA_SUPPORT: role has fewer than two observed states");}}

static bool self_test(){
    for(int i=0;i<K;++i) if(status_id(STATUS[i])!=i) return false;
    Xoshiro x{{1,2,3,4}}; if(x.next()!=11520ULL) return false;
    std::array<uint64_t,4> m={1,2,3,4}; auto g1=stream_from_master(m,1,2,3),g2=stream_from_master(m,1,2,3);for(int i=0;i<20;++i)if(g1.next()!=g2.next())return false;
    Xoshiro bg=stream_from_master(m,1,1,0);for(int i=0;i<1000;++i)if(bg.bounded(7)>=7)return false;std::vector<int> vv={0,1,2,3,4,5};fisher_yates(vv,bg);std::sort(vv.begin(),vv.end());for(int i=0;i<6;++i)if(vv[i]!=i)return false;
    std::ostringstream ss; ss << "AL012000, TEST, 12,\n";
    std::array<std::string,12> st={"TD","TS","HU","EX","SD","SS","LO","WV","DB","XX","TD","TS"};
    std::array<std::string,12> dt={"20000101","20000101","20000101","20000101","20000102","20000102","20000102","20000102","20000103","20000103","20000104","20000104"};
    std::array<std::string,12> tm={"0000","0600","1200","1800","0000","0600","1200","1800","0000","0600","0000","0600"};
    for(int i=0;i<12;++i) ss<<dt[i]<<", "<<tm[i]<<", , "<<st[i]<<", 0, 0N, 0W, 0, 0, 0,\n";
    std::istringstream si(ss.str());auto p=parse_hurdat(si);if(p.triples.size()!=3||p.audit.unrecognized_status_breaks!=1||p.audit.continuity_breaks<1)return false;
    std::ostringstream leapss; leapss << "AL022020, LEAP, 6,\n";
    std::array<std::string,6> ldate={"20200228","20200229","20200229","20200229","20200229","20200301"};
    std::array<std::string,6> ltime={"1800","0000","0600","1200","1800","0000"};
    for(int i=0;i<6;++i) leapss<<ldate[i]<<", "<<ltime[i]<<", , TD, 0, 0N, 0W, 0, 0, 0,\n";
    std::istringstream leapi(leapss.str()); auto lp=parse_hurdat(leapi); if(lp.triples.size()!=2||lp.audit.continuity_breaks!=0)return false;
    BigUInt bp=BigUInt::mul(BigUInt(std::numeric_limits<uint64_t>::max()),BigUInt(std::numeric_limits<uint64_t>::max()));
    if(bp.w!=std::vector<uint32_t>({1U,0U,0xfffffffeU,0xffffffffU}))return false;
    BigUInt bd; bd.w={123U,456U,16U}; Xoshiro ug=stream_from_master(m,2,5,17); for(int i=0;i<256;++i)if(BigUInt::cmp(uniform_big(bd,ug),bd)>=0)return false;
    std::vector<Triple> z;for(int a=0;a<2;++a)for(int c=0;c<2;++c)for(int r=0;r<10;++r)z.push_back(Triple{(uint8_t)a,0,(uint8_t)c});if(std::fabs(g2_uncond(z,0,2))>1e-10L)return false;
    std::vector<Triple> dep;for(int a=0;a<2;++a)for(int r=0;r<20;++r)dep.push_back(Triple{(uint8_t)a,0,(uint8_t)a});if(!(g2_uncond(dep,0,2)>1.0L))return false;
    std::vector<Triple> syn;for(int a=0;a<3;++a)for(int b=0;b<3;++b)for(int c=0;c<3;++c)for(int r=0;r<1+a+b+c;++r)syn.push_back(Triple{(uint8_t)a,(uint8_t)b,(uint8_t)c});auto cc=make_counts(syn);
    for(int h=1;h<=5;++h) if(!exact_q_factorization_checks(cc,h)) return false;
    for(int a=0;a<2;++a)for(int b=0;b<2;++b)for(int c=0;c<2;++c){
        auto q2=qrat(cc,2,state_id(a,b,c)); BigUInt n2=big_product64({cc.WAC[a*K+c],cc.WBC[b*K+c]}), d2=big_product64({cc.W,cc.WC[c]}); if(BigUInt::cmp(BigUInt::mul(q2.n,d2),BigUInt::mul(n2,q2.d))!=0)return false;
        auto q4=qrat(cc,4,state_id(a,b,c)); BigUInt n4=big_product64({cc.WAB[a*K+b],cc.WAC[a*K+c]}), d4=big_product64({cc.W,cc.WA[a]}); if(BigUInt::cmp(BigUInt::mul(q4.n,d4),BigUInt::mul(n4,q4.d))!=0)return false;
    }
    std::array<int,5> ex1={9,100,200,300,400};auto hr=holm(ex1,4999);if(!hr[0])return false;
    std::array<int,5> ex2={10,100,200,300,400};auto hr2=holm(ex2,4999);if(hr2[0])return false;
    ParsedData sp; for(int r=0;r<20;++r){std::vector<int> run;for(int i=0;i<6;++i){Triple t{(uint8_t)((i+r)%3),(uint8_t)((2*i+r)%3),(uint8_t)((i+2*r)%3)};sp.triples.push_back(t);run.push_back(state_id(t.a,t.b,t.c));}sp.block_runs.push_back(run);}sp.audit.retained_triples=sp.triples.size();
    auto c1=run_cal1(sp,m,3);auto c2=run_cal2(sp,m,2);(void)c1;(void)c2;
    return true;
}

static void print_audit(const ParsedData& p){
    std::cout<<"STORMS="<<p.audit.storms<<"\nRAW_RECORDS="<<p.audit.raw_records<<"\nIN_RANGE_RECORDS="<<p.audit.in_range_records
             <<"\nSTANDARD_RECORDS="<<p.audit.standard_records<<"\nRECOGNIZED_RECORDS="<<p.audit.recognized_records
             <<"\nUNRECOGNIZED_STATUS_BREAKS="<<p.audit.unrecognized_status_breaks<<"\nCONTINUITY_BREAKS="<<p.audit.continuity_breaks
             <<"\nRUNS="<<p.audit.runs<<"\nRETAINED_TRIPLES="<<p.audit.retained_triples
             <<"\nTRAILING_RECORDS_DISCARDED="<<p.audit.trailing_records_discarded<<"\n";
}
static int run_analyze(const std::string& file,const std::string& seedhex,bool parse_only){
    std::ifstream f(file);if(!f)throw std::runtime_error("cannot open input");auto p=parse_hurdat(f);print_audit(p);support_gate(p);if(parse_only){std::cout<<"PGH_HURDAT2_PARSE_QUALIFICATION=PASS\n";return 0;}
    auto m=parse_master_hex(seedhex);std::array<long double,5> obs{};for(int h=1;h<=5;++h){obs[h-1]=stat_h(p.triples,h);std::cout<<"H"<<h<<"_G2="<<std::setprecision(20)<<obs[h-1]<<"\n";}
    auto c1=run_cal1(p,m,CAL1_REPS);auto c2=run_cal2(p,m,CAL2_REPS);
    int surv=0,ref=0,inc=0;
    for(int i=0;i<5;++i){std::cout<<"H"<<i+1<<"_CAL1_EXCEED="<<c1.exceed[i]<<"\nH"<<i+1<<"_CAL2_EXCEED="<<c2.exceed[i]<<"\nH"<<i+1<<"_CAL1_HOLM_REJECT="<<(c1.reject[i]?"YES":"NO")<<"\nH"<<i+1<<"_CAL2_HOLM_REJECT="<<(c2.reject[i]?"YES":"NO")<<"\n";std::string v;if(c1.reject[i]&&c2.reject[i]){v="REFUTED_ON_COMMON_TARGET";ref++;}else if(!c1.reject[i]&&!c2.reject[i]){v="SURVIVES_COMMON_TARGET_TEST";surv++;}else{v="INCONCLUSIVE_CALIBRATION_DISAGREEMENT";inc++;}std::cout<<"H"<<i+1<<"_VERDICT="<<v<<"\n";}
    std::string fam;if(inc)fam="FAMILY_RESULT_INCONCLUSIVE_IN_RELEVANT_PART";else if(ref==5)fam="CURRENT_FIVE_CANDIDATE_SUCCESSOR_FAMILY_REFUTED_AT_COMMON_TARGET";else if(surv==1)fam="UNIQUE_SURVIVOR_AT_THIS_TARGET__RELATIVE_DISCRIMINATION_ONLY";else fam="PLURALITY_SURVIVES_COMMON_TARGET";
    std::cout<<"FAMILY_VERDICT="<<fam<<"\nSURVIVAL_IS_CONFIRMATION=NO\n";return 0;
}

} // namespace pgh

int main(int argc,char**argv){
    try{
        if(argc==2 && std::string(argv[1])=="--self-test"){bool ok=pgh::self_test();std::cout<<"PGH_HURDAT2_SELF_TEST="<<(ok?"PASS":"FAIL")<<"\n";return ok?0:1;}
        if(argc==3 && std::string(argv[1])=="--parse-only") return pgh::run_analyze(argv[2],std::string(64,'0'),true);
        if(argc==4 && std::string(argv[1])=="--analyze") return pgh::run_analyze(argv[2],argv[3],false);
        std::cerr<<"usage: pgh_hurdat2_five_candidate --self-test | --parse-only FILE | --analyze FILE MASTERSEED64HEX\n";return 2;
    }catch(const std::exception&e){std::cerr<<"PGH_HURDAT2_ERROR="<<e.what()<<"\n";return 1;}
}
