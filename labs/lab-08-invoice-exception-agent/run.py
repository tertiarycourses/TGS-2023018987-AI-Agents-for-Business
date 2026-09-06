from pathlib import Path
import csv,json,math
P=Path(__file__).resolve().parent
def rows(name):
 with (P/name).open(newline='') as f:return list(csv.DictReader(f))
def save(x):
 (P/'output.json').write_text(json.dumps(x,indent=2))
 print(json.dumps(x,indent=2))
from decimal import Decimal
seen=set();out=[]
po={r['po_id']:r for r in rows('purchase-orders.csv')};gr={r['po_id']:r for r in rows('receipts.csv')}
for r in rows('invoices.csv'):
 key=(r['vendor_id'],r['invoice_id']);p=po.get(r['po_id']);g=gr.get(r['po_id'])
 flags=[]
 if key in seen:flags.append('duplicate')
 seen.add(key)
 if not p or not g:flags.append('missing_po_or_receipt');variance=None
 else:
  variance=(Decimal(r['quantity'])-Decimal(g['quantity']))*Decimal(r['unit_price'])
  if variance:flags.append('quantity_mismatch')
  if r['unit_price']!=p['unit_price']:flags.append('price_mismatch')
  if r['vendor_id']!=p['vendor_id']:flags.append('vendor_mismatch')
 out.append({'invoice_id':r['invoice_id'],'row_id':r['row_id'],'variance_sgd':str(variance) if variance is not None else None,'flags':flags,'payment_authorised':False})
save(out)
