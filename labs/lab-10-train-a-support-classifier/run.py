from pathlib import Path
import csv,json,math
P=Path(__file__).resolve().parent
def rows(name):
 with (P/name).open(newline='') as f:return list(csv.DictReader(f))
def save(x):
 (P/'output.json').write_text(json.dumps(x,indent=2))
 print(json.dumps(x,indent=2))
import torch,random
from transformers import BertTokenizerFast,BertConfig,BertForSequenceClassification
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import f1_score,confusion_matrix,accuracy_score
torch.set_num_threads(2);random.seed(42)
splits={s:rows(s+'.csv') for s in ['train','validation','test']}
for a,b in [('train','test'),('train','validation'),('validation','test')]:
 assert not ({r['record_id'] for r in splits[a]} & {r['record_id'] for r in splits[b]})
 assert not ({r['text'] for r in splits[a]} & {r['text'] for r in splits[b]})
tok=BertTokenizerFast(vocab_file=str(P/'vocab.txt'),do_lower_case=True)
def batch(s):
 r=splits[s];return tok([x['text'] for x in r],padding=True,truncation=True,max_length=24,return_tensors='pt'),torch.tensor([int(x['label']) for x in r])
train,y=batch('train');val,vy=batch('validation')
logs=[];best=None;bestscore=-1
for name,lr,drop in [('baseline_settings',.003,.1),('regularised',.001,.3)]:
 torch.manual_seed(42)
 model=BertForSequenceClassification(BertConfig(vocab_size=len(tok),hidden_size=32,num_hidden_layers=2,num_attention_heads=4,intermediate_size=64,max_position_embeddings=64,num_labels=2,hidden_dropout_prob=drop))
 opt=torch.optim.AdamW(model.parameters(),lr=lr,weight_decay=.01)
 epochlog=[]
 for epoch in range(12):
  model.train();opt.zero_grad();out=model(**train,labels=y);out.loss.backward();norm=torch.nn.utils.clip_grad_norm_(model.parameters(),1.0);opt.step()
  model.eval()
  with torch.no_grad():vp=model(**val).logits.argmax(-1).tolist()
  score=f1_score(vy.tolist(),vp,average='macro',zero_division=0)
  epochlog.append({'epoch':epoch+1,'loss':float(out.loss.detach()),'gradient_norm_before_clip':float(norm),'validation_macro_f1':score})
  if score>bestscore:
   bestscore=score;best=name;model.save_pretrained(P/'selected-model');tok.save_pretrained(P/'selected-model')
 logs.append({'strategy':name,'learning_rate':lr,'dropout':drop,'epochs':epochlog})
model=BertForSequenceClassification.from_pretrained(P/'selected-model');model.eval();test,ty=batch('test')
with torch.no_grad():pred=model(**test).logits.argmax(-1).tolist()
cv=CountVectorizer();x=cv.fit_transform([r['text'] for r in splits['train']]);base_model=LogisticRegression(random_state=42).fit(x,y.tolist());bp=base_model.predict(cv.transform([r['text'] for r in splits['test']])).tolist()
def metrics(p):return {'accuracy':accuracy_score(ty,p),'macro_f1':f1_score(ty,p,average='macro',zero_division=0),'confusion_matrix':confusion_matrix(ty,p,labels=[0,1]).tolist()}
(P/'training-log.json').write_text(json.dumps(logs,indent=2))
save({'initialization':'random; training from scratch, not pretrained fine-tuning','synthetic_data':True,'selected_strategy':best,'selection_validation_macro_f1':bestscore,'transformer_test':metrics(pred),'count_baseline_test':metrics(bp),'split_sizes':{s:len(r) for s,r in splits.items()},'limitations':'Tiny synthetic curriculum data; no production quality claim. Vocabulary is a fixed classroom specification, not learned from test labels.'})
