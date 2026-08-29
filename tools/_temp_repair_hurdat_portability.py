from pathlib import Path
import re, hashlib
p=Path('tools/pgh_hurdat2_five_candidate.cpp')
s=p.read_text()
s=s.replace('#include <boost/multiprecision/cpp_int.hpp>\n\nusing boost::multiprecision::cpp_int;\n','')
start=s.index('struct Rat { cpp_int n,d; };')
end=s.index('static int sample_weights', start)
replacement=r'''struct BigUInt {
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
'''
s=s[:start]+replacement+s[end:]
start=s.index('static Rat proposal_prob')
end=s.index('static std::vector<Triple> permute_h', start)
replacement=r'''static Rat proposal_prob(const Counts& c,const Transition& tr,int h,int from,int to){
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

'''
s=s[:start]+replacement+s[end:]
s=s.replace('bool pass=(cpp_int(100)*d*(exceed[i]+1) <= reps+1);','bool pass=(uint64_t(100)*static_cast<uint64_t>(d)*static_cast<uint64_t>(exceed[i]+1) <= static_cast<uint64_t>(reps+1));')
old='''    for(int h=1;h<=5;++h){Rat sum{0,1};for(int s=0;s<STATES;++s)sum=add_rat(sum,qrat(cc,h,s));if(!rat_eq(sum,{1,1}))return false;}\n    for(int a=0;a<2;++a)for(int b=0;b<2;++b)for(int c=0;c<2;++c){\n        auto q2=qrat(cc,2,state_id(a,b,c)); Rat rhs{cpp_int(cc.WAC[a*K+c])*cc.WBC[b*K+c],cpp_int(cc.W)*cc.WC[c]}; if(!rat_eq(q2,rhs))return false;\n        auto q4=qrat(cc,4,state_id(a,b,c)); Rat rhs4{cpp_int(cc.WAB[a*K+b])*cc.WAC[a*K+c],cpp_int(cc.W)*cc.WA[a]}; if(!rat_eq(q4,rhs4))return false;\n    }'''
new='''    for(int h=1;h<=5;++h) if(!exact_q_factorization_checks(cc,h)) return false;\n    for(int a=0;a<2;++a)for(int b=0;b<2;++b)for(int c=0;c<2;++c){\n        auto q2=qrat(cc,2,state_id(a,b,c)); BigUInt n2=big_product64({cc.WAC[a*K+c],cc.WBC[b*K+c]}), d2=big_product64({cc.W,cc.WC[c]}); if(BigUInt::cmp(BigUInt::mul(q2.n,d2),BigUInt::mul(n2,q2.d))!=0)return false;\n        auto q4=qrat(cc,4,state_id(a,b,c)); BigUInt n4=big_product64({cc.WAB[a*K+b],cc.WAC[a*K+c]}), d4=big_product64({cc.W,cc.WA[a]}); if(BigUInt::cmp(BigUInt::mul(q4.n,d4),BigUInt::mul(n4,q4.d))!=0)return false;\n    }'''
if old not in s:
    raise SystemExit('self-test replacement anchor not found')
s=s.replace(old,new)
p.write_text(s)
sha=hashlib.sha256(p.read_bytes()).hexdigest()
a=Path('audits/PGH1_POST_KP_HURDAT2_FIVE_CANDIDATE_ANALYSIS_AND_CUSTODY_PREREGISTRATION_GATE_0_1_0.md')
t=a.read_text()
t=re.sub(r'SOURCE_SHA256 = [0-9a-f]{64}',f'SOURCE_SHA256 = {sha}',t)
a.write_text(t)
print(sha)
