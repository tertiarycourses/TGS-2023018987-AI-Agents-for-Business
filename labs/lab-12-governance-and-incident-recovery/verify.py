from pathlib import Path
import json
P=Path(__file__).resolve().parent
x=json.loads((P/'output.json').read_text())
assert [r['allowed'] for r in x]==[True,False,False,False,False]
print('PASS: Lab 12 deterministic checks; inspect learner LLM evidence separately.')
