from firebase_admin import db

project_id = "registro-nota"
ref = db.reference('notas')

class MainHandler(tornado.web.RequestHandler):
    def post(self):
        turma = self.get_argument('turma', '')

        saveNotes(turma)

def saveNotes(turma):
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

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8080)
    tornado.ioloop.IOLoop.current().start()
