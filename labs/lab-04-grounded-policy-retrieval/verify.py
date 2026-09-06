from pathlib import Path
import json
P=Path(__file__).resolve().parent
x=json.loads((P/'output.json').read_text())
assert len(x)==3 and all('requires_claim_verification' in r for r in x)
print('PASS: Lab 04 deterministic checks; inspect learner LLM evidence separately.')
