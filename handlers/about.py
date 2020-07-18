from tornado.web import RequestHandler

class AboutHandler(RequestHandler):
    def get(self):
        self.render("about.html")