from pathlib import Path
import json
P=Path(__file__).resolve().parent
x=json.loads((P/'output.json').read_text())
assert x[0]['ok'] and all(not r['ok'] for r in x[1:])
print('PASS: Lab 05 deterministic checks; inspect learner LLM evidence separately.')
