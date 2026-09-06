from pathlib import Path
import csv,json,math
P=Path(__file__).resolve().parent
def rows(name):
 with (P/name).open(newline='') as f:return list(csv.DictReader(f))
def save(x):
 (P/'output.json').write_text(json.dumps(x,indent=2))
 print(json.dumps(x,indent=2))
from tools import execute
save([execute(x) for x in [{'tool':'lookup_order','arguments':{'order_id':'O-104'}},{'tool':'lookup_order','arguments':{'order_id':'O-999'}},{'tool':'issue_refund','arguments':{}},{'tool':'lookup_order','arguments':{'order_id':'O-104','extra':True}}]])
