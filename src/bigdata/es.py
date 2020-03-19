from elasticsearch import Elasticsearch
from datetime import datetime


def push_data(m,es):
	try:
		m['issue_date'] = datetime.strptime(m['issue_date'],'%m/%d/%Y')
		m['fine_amount'] = float(m['fine_amount'])
		m['penalty_amount'] = int(m['penalty_amount'])
		m['interest_amount'] = float(m['interest_amount'])
		m['payment_amount'] = int(m['payment_amount'])
		m['amount_due'] = int(m['amount_due'])
	except Exception:
		pass

	result = es.index(index = 'nyc_data5', doc_type='parking_violation', body = m)
	
	print(result['result'])
		