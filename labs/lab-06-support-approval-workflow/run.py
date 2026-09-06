from pathlib import Path
import csv,json,math
P=Path(__file__).resolve().parent
def rows(name):
 with (P/name).open(newline='') as f:return list(csv.DictReader(f))
def save(x):
 (P/'output.json').write_text(json.dumps(x,indent=2))
 print(json.dumps(x,indent=2))
ledger={};out=[]
for r in rows('requests.csv'):
 key=r['operation_id']
 if key in ledger:state='duplicate_previous_request'
 elif r['receipt']!='true':state='needs_receipt'
 else:state='pending_human_approval';ledger[key]={'state':state,'amount':r['amount_sgd']}
 out.append({'request_id':r['request_id'],'state':state,'executed':False})
save({'simulation':True,'requests':out,'ledger':ledger})
