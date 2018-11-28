from flask import Flask
from flask import request
import base64
import json

app = Flask(__name__)

@app.route('/')
def home():    
	return 'Calcular nota service', 200

@app.route('/calcular', methods=['POST'])
def publish():
	payload = request.get_json()
	message_body = base64.b64decode(str(payload['message']['data'])).decode('utf-8').replace("'", '"')
	array_notas = json.loads(message_body)
	
	print('Email enviado: TESTE!! TESTE!!', array_notas)
	
	return 'ok', 200

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)

