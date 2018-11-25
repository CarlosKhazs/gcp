import tornado.ioloop
import tornado.web
import requests

datastoreURL = "https://get-week-results.appspot.com/"

class SaveCache(tornado.web.RequestHandler):
    def get(self):
        turma = self.get_argument('turma', '')

        saveCache()

class GetWeekResults(tornado.web.RequestHandler):
    def get(self):
        turma = self.get_argument('turma', '')

        generateWeekResults(turma)

def generateWeekResults(turma):
    global datastoreURL
    r = requests.get(datastoreURL)

    print(r.status_code)
    print(r.headers)
    print(r.content)

def saveCache():
    print('Turma salva no cache.')

def make_app():
    return tornado.web.Application([
        (r"/save-cache", SaveCache),
        (r"/get-week-results", GetWeekResults)
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8080)
    tornado.ioloop.IOLoop.current().start()
