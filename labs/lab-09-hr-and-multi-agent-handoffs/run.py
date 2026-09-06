from pathlib import Path
import csv,json,math
P=Path(__file__).resolve().parent
def rows(name):
 with (P/name).open(newline='') as f:return list(csv.DictReader(f))
def save(x):
 (P/'output.json').write_text(json.dumps(x,indent=2))
 print(json.dumps(x,indent=2))
save({'task_id':'ONBOARD-S01','checklist':[r for r in rows('hr-policies.csv') if r['role']=='operations_assistant'],'owner_role':'HR reviewer'})
