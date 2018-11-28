from flask import Flask
from flask import request
from firebase_admin import db
import base64
import json

ref = db.reference('notas')
        
app = Flask(__name__)

@app.route('/')
def home():    
	return 'Firebase service', 200

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
		users_ref = ref.child(key)
	    users_ref.set({
			'matricula': key,
			'nome': n['nome'],
			'nota': n['nota']
		})
		
		print('Saved {}: '.format(key))

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)

