from pathlib import Path
import csv,json,math
P=Path(__file__).resolve().parent
def rows(name):
 with (P/name).open(newline='') as f:return list(csv.DictReader(f))
def save(x):
 (P/'output.json').write_text(json.dumps(x,indent=2))
 print(json.dumps(x,indent=2))
r=rows('predictions.csv');tp=sum(x['true_label']==x['predicted_label']=='1' for x in r);fn=sum(x['true_label']=='1' and x['predicted_label']=='0' for x in r);fp=sum(x['true_label']=='0' and x['predicted_label']=='1' for x in r);tn=len(r)-tp-fn-fp
runs=rows('runs.csv');success=sum(int(x['success']) for x in runs)
save({'tp':tp,'fn':fn,'fp':fp,'tn':tn,'precision':tp/(tp+fp),'recall':tp/(tp+fn),'accuracy':(tp+tn)/len(r),'success_rate':success/len(runs),'cost_per_success_sgd':sum(float(x['cost_sgd']) for x in runs)/success,'synthetic':True})
