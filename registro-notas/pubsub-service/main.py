from flask import Flask
from flask import request
from google.cloud import pubsub_v1

app = Flask(__name__)

project_id = 'registro-notas-223614'
topic_name = 'publish-note'

@app.route('/')
def home():
	return 'PubSub service'

@app.route('/publish', methods=['POST'])
def publish():
	turma = request.get_json()
	publishUser(turma)
	
	return 'ok', 200

def publishUser(turma):
	publisher = pubsub_v1.PublisherClient()
	topic_path = publisher.topic_path(project_id, topic_name)
	
	data = str(turma).encode('utf-8')
	future = publisher.publish(topic_path, data=data)
	print('Published {} of message ID {}.'.format(turma, future.result()))

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
