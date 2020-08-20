from spwb import app
from spwb.models import Article
from flask import render_template, abort


@app.route('/')
def index():        #主页
    l = []
    for i in Article.query.all():
        l.append((i.id, i.title))
    return render_template("index.html", arts=l)


@app.route('/about')
def about():        #关于页面
    return render_template("about.html")


@app.route('/p/<pid>')
def p(pid):
    """
    文章的访问
    """
    pdat = Article.query.get(pid)
    if pdat == None:
        # 如果没找到
        abort(404)
    return render_template("blog/blog.html", title=pdat.title, content=pdat.content)


