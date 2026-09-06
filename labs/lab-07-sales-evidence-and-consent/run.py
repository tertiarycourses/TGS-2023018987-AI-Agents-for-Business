from pathlib import Path
import csv,json,math
P=Path(__file__).resolve().parent
def rows(name):
 with (P/name).open(newline='') as f:return list(csv.DictReader(f))
def save(x):
 (P/'output.json').write_text(json.dumps(x,indent=2))
 print(json.dumps(x,indent=2))
save([{**r,'score':40*int(r['fit'])+35*int(r['need'])+25*int(r['readiness']),'action':'draft_only' if r['consent']=='true' else 'research_only'} for r in rows('leads.csv')])
