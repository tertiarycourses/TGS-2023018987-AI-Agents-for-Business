from pathlib import Path
import json
P=Path(__file__).resolve().parent
x=json.loads((P/'output.json').read_text())
assert x[0]['variance_sgd']=='50' and 'duplicate' in x[1]['flags']
assert 'missing_po_or_receipt' in x[3]['flags']
print('PASS: Lab 08 deterministic checks; inspect learner LLM evidence separately.')
