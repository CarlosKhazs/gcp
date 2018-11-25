import tornado.ioloop
import tornado.web
from google.cloud import datastore

project_id = "cidade-conectada"

class MainHandler(tornado.web.RequestHandler):
    def post(self):
        carro = self.get_argument('carro', '')

        saveCar(carro)

class GetWeekResults(tornado.web.RequestHandler):
    def get(self):
        getWeekResults()

def getWeekResults():
    print('Relatório gerado.')

def saveCar(carro):
    global project_id

    datastore_client = datastore.Client(project_id)

    kind = 'Placas'
    name = 'placa'
    task_key = datastore_client.key(kind, name)

    task['placa'] = u'{}'.format(carro.get(placa, '123456789'))

    datastore_client.put(task)

    print('Saved {}: {}'.format(task.key.name, task['placa']))

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8080)
    tornado.ioloop.IOLoop.current().start()
