from pathlib import Path
import json
P=Path(__file__).resolve().parent
x=json.loads((P/'output.json').read_text())
assert [r['state'] for r in x['requests']]==['pending_human_approval','needs_receipt','duplicate_previous_request']
assert not any(r['executed'] for r in x['requests'])
print('PASS: Lab 06 deterministic checks; inspect learner LLM evidence separately.')
