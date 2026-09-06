from pathlib import Path
import json
P=Path(__file__).resolve().parent
x=json.loads((P/'output.json').read_text())
assert x['hidden_state_shape'][-1]==32
assert abs(x['geometric_example']['cos_q_d2']-2**-.5)<1e-8
print('PASS: Lab 03 deterministic checks; inspect learner LLM evidence separately.')
