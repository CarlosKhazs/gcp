import tornado.ioloop
import tornado.web
from google.cloud import pubsub

project_id = "cidade-conectada"
topic_name = "projects/cidade-conectada/topics/publish-note"
datastore_endpoint = "https://my-test-project.appspot.com/"
stolen_endpoint = "https://my-test-project.appspot.com/"
calculateNote_endpoint = "https://my-test-project.appspot.com/"

class MainHandler(tornado.web.RequestHandler):
    def post(self):
        carro = self.get_argument('carro', '')

        publish(carro)

def publish(carro):
    global project_id
    global topic_name
    global datastore_endpoint
    global firebase_endpoint
    global calculateNote_endpoint

    publisher = pubsub.PublisherClient()

    topic_path = publisher.topic_path(project_id, topic_name)
    topic = publisher.create_topic(topic_path)

    createSubscription('datastore-service', datastore_endpoint)
    createSubscription('firebase-service', firebase_endpoint)
    createSubscription('calculate-note-service', calculateNote_endpoint)

    print('\nTopic created: {}'.format(topic.name))

    data = str(carro).encode('utf-8')
    future = publisher.publish(topic_path, data=carro)
    print('Published {} of message ID {}.'.format(carro, future.result()))

def createSubscription(subscription_name, endpoint):
    global project_id
    global topic_name

    subscriber = pubsub.SubscriberClient()
    topic_path = subscriber.topic_path(project_id, topic_name)
    subscription_path = subscriber.subscription_path(project_id, subscription_name)

    push_config = pubsub.types.PushConfig(push_endpoint=endpoint)

    subscription = subscriber.create_subscription(subscription_path, topic_path, push_config)

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8080)
    tornado.ioloop.IOLoop.current().start()
