import tornado.ioloop
import tornado.web
import requests

functionURL = "https://send-email.appspot.com/"

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        calculateNotes()

def calculateNotes():
    global functionURL
    r = requests.get(functionURL)

    print(r.status_code)
    print(r.headers)
    print(r.content)

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8080)
    tornado.ioloop.IOLoop.current().start()
