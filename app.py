import os.path
import json

from tornado import ioloop
from tornado.web import Application, RequestHandler

class MyApplication(Application):

    def __init__(self, *args, **kwargs):
        self.history = []
        super().__init__(*args, **kwargs)

class MainHandler(RequestHandler):

    def get(self):
        self.render("template/index.html")

class SubmitHandler(RequestHandler):

    def post(self):
        text = json.loads(self.request.body).get("text") or ""
        count = len([x for x in text if x.lower() in "aeiou"])
        self.application.history.append({"text": text, "count": count})
        self.set_status(200)
        self.finish({"history": self.application.history})

class HistoryHandler(RequestHandler):

    def get(self):
        self.set_status(200)
        self.finish({"history": self.application.history})

if __name__ == "__main__":
    static_path = os.path.join(os.path.dirname(__file__), 'static')
    app = MyApplication([
        (
            r"/",
            MainHandler
        ),
        (
            r"/history",
            HistoryHandler
        ),
        (
            r"/submit",
            SubmitHandler
        )
    ], static_path=static_path)
    app.listen(8888)
    ioloop.IOLoop.current().start()
