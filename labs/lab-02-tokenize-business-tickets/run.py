from pathlib import Path
import csv,json,math
P=Path(__file__).resolve().parent
def rows(name):
 with (P/name).open(newline='') as f:return list(csv.DictReader(f))
def save(x):
 (P/'output.json').write_text(json.dumps(x,indent=2))
 print(json.dumps(x,indent=2))
import torch
from transformers import BertTokenizerFast,BertConfig,BertModel
torch.manual_seed(42);torch.set_num_threads(2)
tokenizer=BertTokenizerFast(vocab_file=str(P/'vocab.txt'),do_lower_case=True)
texts=[r['text'] for r in rows('tickets.csv')]
batch=tokenizer(texts,padding=True,truncation=True,max_length=24,return_tensors='pt')
result={'initialization':'random weights for mechanics only; not pretrained semantics','examples':[{'text':t,'tokens':tokenizer.convert_ids_to_tokens(ids.tolist()),'input_ids':ids.tolist(),'attention_mask':mask.tolist()} for t,ids,mask in zip(texts,batch['input_ids'],batch['attention_mask'])]}
save(result)
