from pathlib import Path
import hashlib,re
p=Path('tools/pgh_hurdat2_five_candidate.cpp')
s=p.read_text()
anchor='''    std::istringstream si(ss.str());auto p=parse_hurdat(si);if(p.triples.size()!=3||p.audit.unrecognized_status_breaks!=1||p.audit.continuity_breaks<1)return false;\n'''
insert=r'''    std::istringstream si(ss.str());auto p=parse_hurdat(si);if(p.triples.size()!=3||p.audit.unrecognized_status_breaks!=1||p.audit.continuity_breaks<1)return false;
    std::ostringstream leapss; leapss << "AL022020, LEAP, 6,\n";
    std::array<std::string,6> ldate={"20200228","20200229","20200229","20200229","20200229","20200301"};
    std::array<std::string,6> ltime={"1800","0000","0600","1200","1800","0000"};
    for(int i=0;i<6;++i) leapss<<ldate[i]<<", "<<ltime[i]<<", , TD, 0, 0N, 0W, 0, 0, 0,\n";
    std::istringstream leapi(leapss.str()); auto lp=parse_hurdat(leapi); if(lp.triples.size()!=2||lp.audit.continuity_breaks!=0)return false;
    BigUInt bp=BigUInt::mul(BigUInt(std::numeric_limits<uint64_t>::max()),BigUInt(std::numeric_limits<uint64_t>::max()));
    if(bp.w!=std::vector<uint32_t>({1U,0U,0xfffffffeU,0xffffffffU}))return false;
    BigUInt bd; bd.w={123U,456U,16U}; Xoshiro ug=stream_from_master(m,2,5,17); for(int i=0;i<256;++i)if(BigUInt::cmp(uniform_big(bd,ug),bd)>=0)return false;
'''
if anchor not in s: raise SystemExit('parser self-test anchor not found')
s=s.replace(anchor,insert,1)
p.write_text(s)
sha=hashlib.sha256(p.read_bytes()).hexdigest()
a=Path('audits/PGH1_POST_KP_HURDAT2_FIVE_CANDIDATE_ANALYSIS_AND_CUSTODY_PREREGISTRATION_GATE_0_1_0.md')
t=a.read_text(); t=re.sub(r'SOURCE_SHA256 = [0-9a-f]{64}',f'SOURCE_SHA256 = {sha}',t); a.write_text(t)
print(sha)
