from pathlib import Path
import json
P=Path(__file__).resolve().parent
x=json.loads((P/'output.json').read_text())
assert x['precision']==.75 and x['recall']==.9 and x['accuracy']==.92
assert abs(x['cost_per_success_sgd']-.4)<1e-8
print('PASS: Lab 11 deterministic checks; inspect learner LLM evidence separately.')
