import tornado.ioloop
import tornado.web
from google.cloud import pubsub
from google.cloud import datastore

project_id = "registro-nota"

class MainHandler(tornado.web.RequestHandler):
    def post(self):
        turma = self.get_argument('turma', '')

        saveNotes(turma)

def saveNotes(turma):
    global project_id

    datastore_client = datastore.Client(project_id)

    kind = 'Notas'
    name = 'nota'
    task_key = datastore_client.key(kind, name)

    for n in turma:
        task = datastore.Entity(key=task_key)
        task['matricula'] = u'{}'.format(n.get(matricula, '123456789'))
        task['nome'] = u'{}'.format(n.get(nome, 'WyllerXD'))
        task['nota'] = n.get(nota, 0)

        datastore_client.put(task)

        print('Saved {}: {}'.format(task.key.name, task['nome']))

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8080)
    tornado.ioloop.IOLoop.current().start()
