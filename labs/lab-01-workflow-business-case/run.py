from pathlib import Path
import csv,json,math
P=Path(__file__).resolve().parent
def rows(name):
 with (P/name).open(newline='') as f:return list(csv.DictReader(f))
def save(x):
 (P/'output.json').write_text(json.dumps(x,indent=2))
 print(json.dumps(x,indent=2))
save([{**r,'hours_released':round(int(r['volume_per_month'])*(float(r['manual_minutes'])-float(r['review_minutes']))/60,2)} for r in rows('processes.csv')])
