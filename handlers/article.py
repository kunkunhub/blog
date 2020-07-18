from tornado.web import RequestHandler
import sys
sys.path.append("F:\程序\git\spwb\methods")
#from db import get_article
class ArticleHandler(RequestHandler):
    def get(self, input):
        self.write(get_article(int(input))[1])
