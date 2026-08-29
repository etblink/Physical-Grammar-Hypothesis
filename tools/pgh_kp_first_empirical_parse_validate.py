#!/usr/bin/env python3
from pathlib import Path
from datetime import datetime, timezone, timedelta
import hashlib, json, statistics

ROOT = Path('/mnt/data/pgh_kp_custody')
OUT = Path('/mnt/data/pgh_kp_execution')
START_YEAR, END_YEAR = 1932, 2025
ALLOWED_CODES = [0,3] + [v for n in range(1,9) for v in (10*n-3,10*n,10*n+3)] + [87,90]
assert len(ALLOWED_CODES)==28 and len(set(ALLOWED_CODES))==28
CODE_TO_TOKEN = {0:'0o',3:'0+'}
for n in range(1,9):
    CODE_TO_TOKEN[10*n-3] = f'{n}-'
    CODE_TO_TOKEN[10*n] = f'{n}o'
    CODE_TO_TOKEN[10*n+3] = f'{n}+'
CODE_TO_TOKEN[87]='9-'; CODE_TO_TOKEN[90]='9o'
assert set(CODE_TO_TOKEN)==set(ALLOWED_CODES)

records=[]
file_summaries=[]
errors=[]
for year in range(START_YEAR, END_YEAR+1):
    p=ROOT/'raw'/f'Kp_def{year}.wdc'
    data=[]
    with p.open('r', encoding='ascii', newline='') as f:
        for lineno, raw in enumerate(f,1):
            line=raw.rstrip('\r\n')
            if not line or line.startswith('#'):
                continue
            if len(line) < 28:
                errors.append(f'{p.name}:{lineno}: short data line {len(line)}')
                continue
            try:
                yy=int(line[0:2]); mm=int(line[2:4]); dd=int(line[4:6])
                codes=[int(line[i:i+2]) for i in range(12,28,2)]
            except Exception as e:
                errors.append(f'{p.name}:{lineno}: parse error {e}')
                continue
            full_year = 1900+yy if yy>=32 else 2000+yy
            if full_year != year:
                errors.append(f'{p.name}:{lineno}: year mismatch field={full_year} filename={year}')
            try:
                d=datetime(year,mm,dd,tzinfo=timezone.utc)
            except Exception as e:
                errors.append(f'{p.name}:{lineno}: invalid date {e}')
                continue
            bad=[c for c in codes if c not in CODE_TO_TOKEN]
            if bad:
                errors.append(f'{p.name}:{lineno}: invalid Kp codes {bad}')
            data.append((d,codes))
    # exact date coverage within each year
    expected_days=(datetime(year+1,1,1,tzinfo=timezone.utc)-datetime(year,1,1,tzinfo=timezone.utc)).days
    if len(data)!=expected_days:
        errors.append(f'{p.name}: data day count {len(data)} != {expected_days}')
    if data:
        for j,(d,codes) in enumerate(data):
            exp=datetime(year,1,1,tzinfo=timezone.utc)+timedelta(days=j)
            if d!=exp:
                errors.append(f'{p.name}: day index {j} date {d.isoformat()} != {exp.isoformat()}')
            for slot,c in enumerate(codes):
                ts=d+timedelta(hours=3*slot)
                records.append((ts, CODE_TO_TOKEN.get(c, f'INVALID_{c}'), 'def', c))
    file_summaries.append({'year':year,'days':len(data),'expected_days':expected_days})

# global schedule checks
expected_start=datetime(1932,1,1,tzinfo=timezone.utc)
expected_end=datetime(2025,12,31,21,tzinfo=timezone.utc)
expected_count=274672
if len(records)!=expected_count:
    errors.append(f'record count {len(records)} != {expected_count}')
seen=set()
dupes=0
for i,(ts,token,status,code) in enumerate(records):
    exp=expected_start+timedelta(hours=3*i)
    if ts!=exp:
        errors.append(f'grid mismatch at record {i}: {ts.isoformat()} != {exp.isoformat()}')
        if len(errors)>100: break
    if ts in seen: dupes+=1
    seen.add(ts)
if records:
    if records[0][0]!=expected_start: errors.append('first timestamp mismatch')
    if records[-1][0]!=expected_end: errors.append('last timestamp mismatch')
if dupes: errors.append(f'duplicate timestamps {dupes}')
observed_tokens=sorted({r[1] for r in records}, key=lambda t: ALLOWED_CODES.index(next(k for k,v in CODE_TO_TOKEN.items() if v==t)))
if set(observed_tokens)!=set(CODE_TO_TOKEN.values()):
    errors.append(f'observed native alphabet differs: {observed_tokens}')

# deterministic normalized serialization chosen before statistical analysis.
norm=OUT/'Kp_def_1932_2025.normalized.tsv'
with norm.open('w', encoding='ascii', newline='\n') as f:
    f.write('timestamp_utc\tkp_token\tstatus\n')
    for ts,token,status,code in records:
        f.write(ts.strftime('%Y-%m-%dT%H:%M:%SZ')+f'\t{token}\t{status}\n')
sha_norm=hashlib.sha256(norm.read_bytes()).hexdigest()
sha_raw=hashlib.sha256((ROOT/'Kp_def_1932_2025.wdc.concat').read_bytes()).hexdigest()

# scheduled non-overlapping blocks, no time compression
max_blocks=len(records)//3
trailing=len(records)%3
retained=[]; discarded=[]
for k in range(max_blocks):
    tri=records[3*k:3*k+3]
    # all parsed records are from definitive DOI files; status retained explicitly
    if len(tri)==3 and all(x[2]=='def' and not x[1].startswith('INVALID_') for x in tri):
        retained.append((k,tri[0],tri[1],tri[2]))
    else:
        discarded.append(k)
# segment lengths of adjacent retained scheduled blocks
segments=[]
if retained:
    run=1
    prev=retained[0][0]
    for row in retained[1:]:
        k=row[0]
        if k==prev+1: run+=1
        else: segments.append(run); run=1
        prev=k
    segments.append(run)

support={
    'raw_sha256':sha_raw,
    'normalized_sha256':sha_norm,
    'normalized_bytes':norm.stat().st_size,
    'year_files':len(file_summaries),
    'ut_days':sum(x['days'] for x in file_summaries),
    'scheduled_records':len(records),
    'first_timestamp':records[0][0].strftime('%Y-%m-%dT%H:%M:%SZ') if records else None,
    'last_timestamp':records[-1][0].strftime('%Y-%m-%dT%H:%M:%SZ') if records else None,
    'duplicate_timestamps':dupes,
    'native_alphabet_size_expected':28,
    'native_alphabet_size_observed':len(observed_tokens),
    'native_alphabet_observed':observed_tokens,
    'max_nonoverlapping_triples':max_blocks,
    'trailing_unpaired_records':trailing,
    'retained_triples':len(retained),
    'discarded_triples':len(discarded),
    'segment_count':len(segments),
    'segment_lengths':segments,
    'support_minimum_1000_pass':len(retained)>=1000,
    'validation_errors':errors,
}
(OUT/'custody_validation.json').write_text(json.dumps(support,indent=2)+'\n',encoding='utf-8')
# Encode retained triples as code indices 0..27 for analysis.
code_to_idx={c:i for i,c in enumerate(ALLOWED_CODES)}
with (OUT/'retained_triples.tsv').open('w',encoding='ascii',newline='\n') as f:
    f.write('block_index\tA\tB\tC\n')
    for k,a,b,c in retained:
        f.write(f'{k}\t{code_to_idx[a[3]]}\t{code_to_idx[b[3]]}\t{code_to_idx[c[3]]}\n')
print(json.dumps(support,indent=2))
if errors:
    raise SystemExit(2)
