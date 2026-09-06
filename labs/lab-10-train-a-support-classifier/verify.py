from pathlib import Path
import json
P=Path(__file__).resolve().parent
x=json.loads((P/'output.json').read_text())
assert (P/'selected-model/config.json').exists()
assert len(json.loads((P/'training-log.json').read_text()))==2
assert sum(x['split_sizes'].values())==96
print('PASS: Lab 10 deterministic checks; inspect learner LLM evidence separately.')
