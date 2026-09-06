from pathlib import Path
import csv,json,math
P=Path(__file__).resolve().parent
def rows(name):
 with (P/name).open(newline='') as f:return list(csv.DictReader(f))
def save(x):
 (P/'output.json').write_text(json.dumps(x,indent=2))
 print(json.dumps(x,indent=2))
out=[]
for r in rows('attack-cases.csv'):
 allowed=r['enabled']=='true' and r['customer']=='C-01' and r['tool'] in ['lookup_order','issue_refund'] and (r['tool']!='issue_refund' or r['approved']=='true')
 out.append({'case_id':r['case_id'],'allowed':allowed,'simulation':True,'note':'Approval column represents a trusted harness input, never a model assertion.'})
save(out)
