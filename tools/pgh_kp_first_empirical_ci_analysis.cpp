#include <algorithm>
#include <array>
#include <cmath>
#include <cstdint>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <limits>
#include <numeric>
#include <random>
#include <sstream>
#include <stdexcept>
#include <string>
#include <vector>

static constexpr int S = 28;
static constexpr int CELLS = S*S*S;
static constexpr int PAIRS = S*S;
static constexpr int P1_REPS = 4999;
static constexpr int P2_REPS = 1999;
static constexpr double ALPHA = 0.01;
static constexpr double JEFF = 0.5;
// first_64_bits(SHA256(PREREGISTRATION_COMMIT_SHA || label)), interpreted as an unsigned big-endian integer.
static constexpr uint64_t SEED_PERM = 9631348867133756348ULL;
static constexpr uint64_t SEED_MARKOV = 2988388260916591174ULL;

static const std::array<const char*,S> TOKENS = {
  "0o","0+","1-","1o","1+","2-","2o","2+","3-","3o","3+","4-","4o","4+",
  "5-","5o","5+","6-","6o","6+","7-","7o","7+","8-","8o","8+","9-","9o"
};

struct Triple { uint32_t block; uint8_t a,b,c; };

// Deterministic MT19937-64 implementation choice locked before computing any statistic.
// We avoid std::uniform_* and std::shuffle so mapping from engine output to samples is explicit.
struct DRng {
  std::mt19937_64 eng;
  explicit DRng(uint64_t seed): eng(seed) {}
  uint64_t next() { return eng(); }
  uint64_t bounded(uint64_t bound) {
    if (bound == 0) throw std::runtime_error("bounded(0)");
    const uint64_t threshold = uint64_t(-bound) % bound;
    for (;;) {
      uint64_t r = next();
      if (r >= threshold) return r % bound;
    }
  }
  double unit53() {
    // exact [0,1) conversion using the high 53 bits.
    return double(next() >> 11) * (1.0 / 9007199254740992.0);
  }
};

struct Alias {
  std::array<double,S> prob{};
  std::array<uint8_t,S> alias{};
};

Alias make_alias(const std::array<double,S>& p) {
  Alias t;
  std::array<double,S> scaled{};
  std::vector<int> small, large;
  small.reserve(S); large.reserve(S);
  double sum = std::accumulate(p.begin(), p.end(), 0.0);
  if (!(sum > 0)) throw std::runtime_error("nonpositive categorical sum");
  for (int i=0;i<S;++i) {
    scaled[i] = p[i] * S / sum;
    t.alias[i] = (uint8_t)i;
    if (scaled[i] < 1.0) small.push_back(i); else large.push_back(i);
  }
  while (!small.empty() && !large.empty()) {
    int s = small.back(); small.pop_back();
    int l = large.back(); large.pop_back();
    t.prob[s] = scaled[s];
    t.alias[s] = (uint8_t)l;
    scaled[l] = (scaled[l] + scaled[s]) - 1.0;
    if (scaled[l] < 1.0) small.push_back(l); else large.push_back(l);
  }
  while (!large.empty()) { int i=large.back(); large.pop_back(); t.prob[i]=1.0; t.alias[i]=(uint8_t)i; }
  while (!small.empty()) { int i=small.back(); small.pop_back(); t.prob[i]=1.0; t.alias[i]=(uint8_t)i; }
  return t;
}

inline uint8_t sample_alias(const Alias& t, DRng& rng) {
  uint64_t col = rng.bounded(S);
  return (rng.unit53() < t.prob[col]) ? (uint8_t)col : t.alias[col];
}

struct Counts {
  std::array<uint32_t,CELLS> abc{};
  std::array<uint32_t,PAIRS> ab{};
  std::array<uint32_t,PAIRS> bc{};
  std::array<uint32_t,S> b{};
  uint64_t N=0;
};

inline int idx3(int a,int b,int c){ return (a*S+b)*S+c; }
inline int idx2(int x,int y){ return x*S+y; }

Counts count_triples(const std::vector<Triple>& x, size_t lo=0, size_t hi=std::numeric_limits<size_t>::max()) {
  Counts c;
  hi = std::min(hi, x.size());
  for (size_t i=lo;i<hi;++i) {
    int a=x[i].a,b=x[i].b,d=x[i].c;
    ++c.abc[idx3(a,b,d)]; ++c.ab[idx2(a,b)]; ++c.bc[idx2(b,d)]; ++c.b[b]; ++c.N;
  }
  return c;
}

double g2_from_counts(const Counts& c, std::array<double,S>* by_b=nullptr) {
  if (by_b) by_b->fill(0.0);
  double g=0.0;
  for (int a=0;a<S;++a) for (int b=0;b<S;++b) for (int d=0;d<S;++d) {
    uint32_t n=c.abc[idx3(a,b,d)];
    if (!n) continue;
    uint32_t nb=c.b[b], nab=c.ab[idx2(a,b)], nbc=c.bc[idx2(b,d)];
    double term = 2.0 * double(n) * std::log((double(n)*double(nb))/(double(nab)*double(nbc)));
    g += term;
    if (by_b) (*by_b)[b] += term;
  }
  return g;
}

double g2_p1_joint(const std::array<uint32_t,CELLS>& abc, const Counts& fixed) {
  double g=0.0;
  for (int a=0;a<S;++a) for (int b=0;b<S;++b) for (int d=0;d<S;++d) {
    uint32_t n=abc[idx3(a,b,d)];
    if (!n) continue;
    g += 2.0 * double(n) * std::log((double(n)*double(fixed.b[b])) /
      (double(fixed.ab[idx2(a,b)])*double(fixed.bc[idx2(b,d)])));
  }
  return g;
}

double h_c_given_b_bits(const Counts& c) {
  if (!c.N) return std::numeric_limits<double>::quiet_NaN();
  double h=0.0;
  for (int b=0;b<S;++b) for (int d=0;d<S;++d) {
    uint32_t nbc=c.bc[idx2(b,d)];
    if (!nbc) continue;
    double p = double(nbc)/double(c.N);
    double q = double(nbc)/double(c.b[b]);
    h -= p*std::log2(q);
  }
  return h;
}

double median_sorted(const std::vector<double>& v) {
  size_t n=v.size();
  if (n%2) return v[n/2];
  return 0.5*(v[n/2-1]+v[n/2]);
}
double nearest_rank_99_sorted(const std::vector<double>& v) {
  size_t rank = (size_t)std::ceil(0.99 * double(v.size())); // 1-based
  if (rank<1) rank=1;
  if (rank>v.size()) rank=v.size();
  return v[rank-1];
}

std::string verdict(double pp,double pm) {
  if (pp <= ALPHA && pm <= ALPHA) return "REFUTED_AT_KP_TARGET";
  if (pp > ALPHA && pm > ALPHA) return "SURVIVES_FIRST_KP_TEST";
  return "INCONCLUSIVE_CALIBRATION_DISAGREEMENT";
}

int main(int argc,char**argv){
  if (argc!=2) { std::cerr<<"usage: kp_ci_analysis retained_triples.tsv\n"; return 2; }
  if (SEED_PERM==0 || SEED_MARKOV==0) throw std::runtime_error("mechanical seeds not injected");
  std::ifstream in(argv[1]); if(!in) throw std::runtime_error("cannot open triples");
  std::string line; std::getline(in,line); // header
  std::vector<Triple> x;
  while(std::getline(in,line)){
    if(line.empty()) continue;
    std::istringstream ss(line); unsigned block,a,b,c;
    if(!(ss>>block>>a>>b>>c)) throw std::runtime_error("bad triple row");
    if(a>=S||b>=S||c>=S) throw std::runtime_error("state out of range");
    x.push_back(Triple{block,(uint8_t)a,(uint8_t)b,(uint8_t)c});
  }
  if(x.size()<1000) throw std::runtime_error("INCONCLUSIVE_DATA_SUPPORT");

  Counts obs=count_triples(x);
  std::array<double,S> by_b{};
  double gobs=g2_from_counts(obs,&by_b);
  double ibits=gobs/(2.0*double(obs.N)*std::log(2.0));
  double hcb=h_c_given_b_bits(obs);
  double M=(hcb>0)? ibits/hcb : std::numeric_limits<double>::quiet_NaN();
  size_t split=x.size()/2; // value-independent operational rule: floor(N/2) in first half, remainder in second.
  Counts c1=count_triples(x,0,split), c2=count_triples(x,split,x.size());
  double g1=g2_from_counts(c1), g2=g2_from_counts(c2);
  double i1=g1/(2.0*double(c1.N)*std::log(2.0));
  double i2=g2/(2.0*double(c2.N)*std::log(2.0));

  // Sparse support diagnostics.
  std::vector<uint32_t> occ;
  for(auto n:obs.abc) if(n) occ.push_back(n);
  std::sort(occ.begin(),occ.end());
  double medcell = occ.size()%2 ? occ[occ.size()/2] : 0.5*(occ[occ.size()/2-1]+occ[occ.size()/2]);
  uint32_t maxcell = occ.empty()?0:occ.back();
  int b_lt2=0,b_lt5=0,b_lt10=0,b_lt50=0;
  for(auto n:obs.b){ if(n<2)++b_lt2; if(n<5)++b_lt5; if(n<10)++b_lt10; if(n<50)++b_lt50; }

  // P1: fixed-margin within-B Fisher-Yates permutations of C.
  std::array<std::vector<size_t>,S> pos;
  std::vector<uint8_t> baseC(x.size()), permC(x.size());
  for(size_t i=0;i<x.size();++i){ pos[x[i].b].push_back(i); baseC[i]=x[i].c; }
  DRng rng1(SEED_PERM);
  std::vector<double> p1; p1.reserve(P1_REPS);
  int ge1=0;
  std::array<uint32_t,CELLS> joint{};
  for(int r=0;r<P1_REPS;++r){
    permC=baseC;
    for(int b=0;b<S;++b){
      const auto& p=pos[b];
      for(size_t ii=p.size(); ii>1; --ii){
        size_t j=(size_t)rng1.bounded(ii);
        std::swap(permC[p[ii-1]],permC[p[j]]);
      }
    }
    joint.fill(0);
    for(size_t i=0;i<x.size();++i) ++joint[idx3(x[i].a,x[i].b,permC[i])];
    double g=g2_p1_joint(joint,obs); p1.push_back(g); if(g>=gobs) ++ge1;
  }
  double pperm=(1.0+ge1)/(1.0+P1_REPS);

  // P2: fit 3 phase-aware first-order Markov null with Jeffreys 1/2 smoothing.
  std::array<std::array<uint64_t,S>,S> n0{},n1{},n2{};
  std::array<uint64_t,S> ninit{};
  std::vector<size_t> seg_starts{0};
  std::vector<size_t> seg_lengths;
  for(size_t i=0;i<x.size();++i){ ++n0[x[i].a][x[i].b]; ++n1[x[i].b][x[i].c]; }
  size_t run=1;
  ++ninit[x[0].a];
  for(size_t i=0;i+1<x.size();++i){
    if(x[i+1].block==x[i].block+1){ ++n2[x[i].c][x[i+1].a]; ++run; }
    else { seg_lengths.push_back(run); seg_starts.push_back(i+1); run=1; ++ninit[x[i+1].a]; }
  }
  seg_lengths.push_back(run);
  std::array<Alias,S> a0{},a1{},a2{};
  for(int row=0;row<S;++row){
    std::array<double,S> p0{},p1a{},p2a{};
    for(int col=0;col<S;++col){ p0[col]=double(n0[row][col])+JEFF; p1a[col]=double(n1[row][col])+JEFF; p2a[col]=double(n2[row][col])+JEFF; }
    a0[row]=make_alias(p0); a1[row]=make_alias(p1a); a2[row]=make_alias(p2a);
  }
  std::array<double,S> pinit{}; for(int s=0;s<S;++s) pinit[s]=double(ninit[s])+JEFF;
  Alias ainit=make_alias(pinit);

  DRng rng2(SEED_MARKOV);
  std::vector<double> p2v; p2v.reserve(P2_REPS);
  int ge2=0;
  for(int r=0;r<P2_REPS;++r){
    Counts sim;
    for(size_t seg=0;seg<seg_lengths.size();++seg){
      uint8_t A=sample_alias(ainit,rng2);
      size_t L=seg_lengths[seg];
      for(size_t k=0;k<L;++k){
        uint8_t B=sample_alias(a0[A],rng2);
        uint8_t C=sample_alias(a1[B],rng2);
        ++sim.abc[idx3(A,B,C)]; ++sim.ab[idx2(A,B)]; ++sim.bc[idx2(B,C)]; ++sim.b[B]; ++sim.N;
        if(k+1<L) A=sample_alias(a2[C],rng2);
      }
    }
    double g=g2_from_counts(sim); p2v.push_back(g); if(g>=gobs) ++ge2;
  }
  double pmarkov=(1.0+ge2)/(1.0+P2_REPS);

  std::ofstream f1("P1_G2_NULL.tsv"); f1<<std::setprecision(17)<<"replicate\tG2\n"; for(size_t i=0;i<p1.size();++i) f1<<(i+1)<<'\t'<<p1[i]<<'\n';
  std::ofstream f2("P2_G2_NULL.tsv"); f2<<std::setprecision(17)<<"replicate\tG2\n"; for(size_t i=0;i<p2v.size();++i) f2<<(i+1)<<'\t'<<p2v[i]<<'\n';
  auto p1s=p1,p2s=p2v; std::sort(p1s.begin(),p1s.end()); std::sort(p2s.begin(),p2s.end());
  double p1med=median_sorted(p1s), p199=nearest_rank_99_sorted(p1s), p2med=median_sorted(p2s), p299=nearest_rank_99_sorted(p2s);

  std::vector<int> order(S); std::iota(order.begin(),order.end(),0);
  std::stable_sort(order.begin(),order.end(),[&](int u,int v){return by_b[u]>by_b[v];});

  std::cout<<std::setprecision(17);
  std::cout<<"{\n";
  std::cout<<"  \"implementation\": {\"prng\": \"std::mt19937_64\", \"bounded_mapping\": \"rejection_modulo\", \"unit_mapping\": \"high_53_bits_over_2^53\", \"categorical\": \"Vose_alias\", \"p99\": \"nearest_rank\", \"half_split\": \"floor_N_over_2_first\"},\n";
  std::cout<<"  \"seeds\": {\"perm\": "<<SEED_PERM<<", \"markov\": "<<SEED_MARKOV<<"},\n";
  std::cout<<"  \"N\": "<<obs.N<<",\n";
  std::cout<<"  \"occupied_ABC_cells\": "<<occ.size()<<",\n";
  std::cout<<"  \"B_stratum_counts\": ["; for(int b=0;b<S;++b){if(b)std::cout<<",";std::cout<<obs.b[b];} std::cout<<"],\n";
  std::cout<<"  \"B_strata_lt_2\": "<<b_lt2<<", \"B_strata_lt_5\": "<<b_lt5<<", \"B_strata_lt_10\": "<<b_lt10<<", \"B_strata_lt_50\": "<<b_lt50<<",\n";
  std::cout<<"  \"occupied_cell_max_count\": "<<maxcell<<", \"occupied_cell_median_count\": "<<medcell<<",\n";
  std::cout<<"  \"G2_obs\": "<<gobs<<", \"I_bits\": "<<ibits<<", \"H_C_given_B_bits\": "<<hcb<<", \"M\": "<<M<<",\n";
  std::cout<<"  \"halves\": {\"first_N\": "<<c1.N<<", \"first_G2\": "<<g1<<", \"first_I_bits\": "<<i1<<", \"second_N\": "<<c2.N<<", \"second_G2\": "<<g2<<", \"second_I_bits\": "<<i2<<"},\n";
  std::cout<<"  \"per_B_G2_sorted\": [\n"; for(int j=0;j<S;++j){int b=order[j];std::cout<<"    {\"B\": \""<<TOKENS[b]<<"\", \"state_index\": "<<b<<", \"G2\": "<<by_b[b]<<"}"<<(j+1<S?",":"")<<"\n";} std::cout<<"  ],\n";
  std::cout<<"  \"P1\": {\"replicates\": "<<P1_REPS<<", \"ge_obs\": "<<ge1<<", \"p_perm\": "<<pperm<<", \"median_G2\": "<<p1med<<", \"p99_G2\": "<<p199<<", \"obs_minus_median\": "<<(gobs-p1med)<<", \"obs_minus_p99\": "<<(gobs-p199)<<"},\n";
  std::cout<<"  \"P2\": {\"replicates\": "<<P2_REPS<<", \"segments\": "<<seg_lengths.size()<<", \"segment_lengths\": ["; for(size_t i=0;i<seg_lengths.size();++i){if(i)std::cout<<",";std::cout<<seg_lengths[i];} std::cout<<"], \"ge_obs\": "<<ge2<<", \"p_markov\": "<<pmarkov<<", \"median_G2\": "<<p2med<<", \"p99_G2\": "<<p299<<", \"obs_minus_median\": "<<(gobs-p2med)<<", \"obs_minus_p99\": "<<(gobs-p299)<<"},\n";
  std::cout<<"  \"verdict\": \""<<verdict(pperm,pmarkov)<<"\"\n";
  std::cout<<"}\n";
}
