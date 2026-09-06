from pathlib import Path
import csv,json,math
P=Path(__file__).resolve().parent
def rows(name):
 with (P/name).open(newline='') as f:return list(csv.DictReader(f))
def save(x):
 (P/'output.json').write_text(json.dumps(x,indent=2))
 print(json.dumps(x,indent=2))
import re
def words(s):return set(re.findall(r'[a-z]+',s.lower()))-{'a','the','is','in','does','who','it','and'}
result=[]
for q in rows('questions.csv'):
 ranked=sorted(rows('policies.csv'),key=lambda r:len(words(q['question'])&words(r['clause'])),reverse=True)
 hits=[{'policy_id':r['policy_id'],'clause':r['clause']} for r in ranked if words(q['question'])&words(r['clause'])][:2]
 result.append({'question_id':q['question_id'],'retriever':'lexical overlap baseline','hits':hits,'requires_claim_verification':True})
save(result)
