from pathlib import Path
import csv,json,math
P=Path(__file__).resolve().parent
def rows(name):
 with (P/name).open(newline='') as f:return list(csv.DictReader(f))
def save(x):
 (P/'output.json').write_text(json.dumps(x,indent=2))
 print(json.dumps(x,indent=2))
def execute(proposal):
 if set(proposal)!={'tool','arguments'}:return {'ok':False,'error':'invalid envelope'}
 name,args=proposal['tool'],proposal['arguments']
 if not isinstance(args,dict):return {'ok':False,'error':'arguments must be an object'}
 if name=='lookup_order':
  if set(args)!={'order_id'} or not isinstance(args['order_id'],str):return {'ok':False,'error':'invalid arguments'}
  hit=next((r for r in rows('orders.csv') if r['order_id']==args['order_id']),None)
  if not hit or hit['customer_id']!='C-01':return {'ok':False,'error':'not found or not authorised'}
  return {'ok':True,'source':'orders.csv','record':hit}
 if name=='search_policy':
  if set(args)!={'query'} or not isinstance(args['query'],str):return {'ok':False,'error':'invalid arguments'}
  return {'ok':True,'source':'policies.csv','records':[r for r in rows('policies.csv') if r['role']=='support' and any(w.lower() in r['clause'].lower() for w in args['query'].split())]}
 return {'ok':False,'error':'tool denied'}
if __name__=='__main__':
 import sys
 proposal=json.loads(Path(sys.argv[1]).read_text())
 out=execute(proposal);(P/'tool-result.json').write_text(json.dumps(out,indent=2));print(json.dumps(out,indent=2))
