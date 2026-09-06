from pathlib import Path
import json
P=Path(__file__).resolve().parent
x=json.loads((P/'output.json').read_text())
assert all(len(e['input_ids'])==len(e['attention_mask']) for e in x['examples'])
assert '[CLS]' in x['examples'][0]['tokens']
print('PASS: Lab 02 deterministic checks; inspect learner LLM evidence separately.')
