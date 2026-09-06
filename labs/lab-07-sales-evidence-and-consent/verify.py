from pathlib import Path
import json
P=Path(__file__).resolve().parent
x=json.loads((P/'output.json').read_text())
assert x[0]['score']==75 and x[1]['score']==40
assert x[1]['action']=='research_only'
print('PASS: Lab 07 deterministic checks; inspect learner LLM evidence separately.')
