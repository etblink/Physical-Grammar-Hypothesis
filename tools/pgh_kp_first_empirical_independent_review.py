#!/usr/bin/env python3
from pathlib import Path
from collections import Counter
import csv, hashlib, json, math, statistics

ROOT=Path('.')
TOKENS=['0o','0+']+[x for n in range(1,9) for x in (f'{n}-',f'{n}o',f'{n}+')]+['9-','9o']
idx={t:i for i,t in enumerate(TOKENS)}
rows=[]
with open('Kp_def_1932_2025.normalized.tsv',newline='') as f:
    r=csv.DictReader(f,delimiter='\t')
    for row in r:
        assert row['status']=='def'
        assert row['kp_token'] in idx
        rows.append(idx[row['kp_token']])
assert len(rows)==274672
triples=[tuple(rows[i:i+3]) for i in range(0,(len(rows)//3)*3,3)]
assert len(triples)==91557

def stats(ts):
    N=len(ts)
    abc=Counter(ts)
    ab=Counter((a,b) for a,b,c in ts)
    bc=Counter((b,c) for a,b,c in ts)
    nb=Counter(b for a,b,c in ts)
    g=0.0
    byb=Counter()
    for (a,b,c),n in abc.items():
        term=2*n*math.log((n*nb[b])/(ab[(a,b)]*bc[(b,c)]))
        g+=term; byb[b]+=term
    ib=g/(2*N*math.log(2))
    h=0.0
    for (b,c),n in bc.items():
        p=n/N; q=n/nb[b]
        h-=p*math.log2(q)
    return {'N':N,'g':g,'ib':ib,'h':h,'m':ib/h,'abc':abc,'nb':nb,'byb':byb}
full=stats(triples)
split=len(triples)//2
first=stats(triples[:split]); second=stats(triples[split:])
primary=json.load(open('analysis_result.primary.json'))
assert full['N']==primary['N']
for got,key,tol in [(full['g'],'G2_obs',1e-9),(full['ib'],'I_bits',1e-15),(full['h'],'H_C_given_B_bits',1e-14),(full['m'],'M',1e-15)]:
    assert abs(got-primary[key])<=tol, (got,key,primary[key])
assert first['N']==primary['halves']['first_N'] and second['N']==primary['halves']['second_N']
assert abs(first['g']-primary['halves']['first_G2'])<1e-9
assert abs(second['g']-primary['halves']['second_G2'])<1e-9
assert [full['nb'][i] for i in range(28)]==primary['B_stratum_counts']
occ=sorted(full['abc'].values())
med=statistics.median(occ)
assert len(occ)==primary['occupied_ABC_cells']
assert max(occ)==primary['occupied_cell_max_count']
assert med==primary['occupied_cell_median_count']

def read_null(path):
    vals=[]
    with open(path) as f:
        next(f)
        for line in f:
            _,v=line.rstrip().split('\t'); vals.append(float(v))
    return vals
for label,path,reps,pkey in [('P1','P1_G2_NULL.primary.tsv',4999,'p_perm'),('P2','P2_G2_NULL.primary.tsv',1999,'p_markov')]:
    vals=read_null(path); assert len(vals)==reps
    ge=sum(v>=full['g'] for v in vals)
    p=(1+ge)/(1+reps)
    assert ge==primary[label]['ge_obs']
    assert abs(p-primary[label][pkey])<1e-18
    s=sorted(vals)
    med=s[len(s)//2]
    p99=s[math.ceil(.99*len(s))-1]
    assert abs(med-primary[label]['median_G2'])<1e-12
    assert abs(p99-primary[label]['p99_G2'])<1e-12
assert primary['verdict']=='REFUTED_AT_KP_TARGET'
assert primary['P1']['p_perm']<=.01 and primary['P2']['p_markov']<=.01
print(json.dumps({
  'independent_observed_G2':full['g'],
  'independent_I_bits':full['ib'],
  'independent_M':full['m'],
  'P1_recomputed_p':primary['P1']['p_perm'],
  'P2_recomputed_p':primary['P2']['p_markov'],
  'mechanical_verdict':'REFUTED_AT_KP_TARGET',
  'review':'PASS'
},indent=2))
