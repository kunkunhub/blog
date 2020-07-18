from tornado.web import RequestHandler
import sys
sys.path.append("F:\程序\git\spwb\methods")
from db import get_article
class ArticleHandler(RequestHandler):
    def get(self, x):
        a = get_article(x)    
        self.render("blog.html", title=a[0][0], text=a[0][1])

