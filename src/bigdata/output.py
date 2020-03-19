import json
from src.bigdata.es import push_data
from elasticsearch import Elasticsearch

def get_output(output,data):
	if output=='print':
		es = Elasticsearch()
		for m in data:
			push_data(m,es)
			print(m,'\n')
	else:
		try:
			with open(output, 'a') as newfile:
				es = Elasticsearch()
				for m in data:
					newfile.write(json.dumps(m)+'\n')
					push_data(m,es)
		except:
			if output =='':
				print('Please specify your output')
	
