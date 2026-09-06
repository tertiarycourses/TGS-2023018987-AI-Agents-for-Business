from pathlib import Path
import json
P=Path(__file__).resolve().parent
x=json.loads((P/'output.json').read_text())
assert len(x['checklist'])==2
assert all(r['role']=='operations_assistant' for r in x['checklist'])
print('PASS: Lab 09 deterministic checks; inspect learner LLM evidence separately.')
