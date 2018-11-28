from flask import Flask
from flask import request
from google.cloud import datastore
import base64
import json

app = Flask(__name__)

@app.route('/')
def home():
	return 'Datastore service'

@app.route('/salvar', methods=['POST'])
def publish():
	payload = request.get_json()
	message_body = base64.b64decode(str(payload['message']['data'])).decode('utf-8').replace("'", '"')
	array_notas = json.loads(message_body)
	saveNotes(array_notas)
	return 'OK', 200

def saveNotes(array_notas):
	print('NOTAS ', array_notas)
	
	datastore_client = datastore.Client()
	
	kind = 'Notas'

	for n in array_notas:
		key = u'{}'.format(n['matricula'])
		task_key = datastore_client.key(kind, key)
		task = datastore.Entity(key=task_key)
		task['matricula'] = key
		task['nome'] = u'{}'.format(n['nome'])
		task['nota'] = n['nota']
		
		datastore_client.put(task)
		
		print('Saved {}: {}'.format(task.key.name, task['nome']))

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
