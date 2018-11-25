from firebase_admin import db
from google.cloud import datastore

project_id = "cidade-conectada"
ref = db.reference('notas')

class MainHandler(tornado.web.RequestHandler):
    def post(self):
        turma = self.get_argument('turma', '')

        saveNotesFirebase(turma)
        saveNotesDatastore(turma)

def saveNotesFirebase(turma):
    global project_id

    for n in turma:
        users_ref = ref.child(turma)
        users_ref.set({
            n.matricula: {
                'nome': n.nome,
                'nota': n.nota
            }
        })

        print('Saved {}: {}'.format(n['nome']))

def saveNotesDatastore(turma):
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
