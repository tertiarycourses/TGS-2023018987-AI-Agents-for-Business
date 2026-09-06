from pathlib import Path
import json
P=Path(__file__).resolve().parent
x=json.loads((P/'output.json').read_text())
assert abs(x[0]['hours_released']-83.33)<.01
print('PASS: Lab 01 deterministic checks; inspect learner LLM evidence separately.')
