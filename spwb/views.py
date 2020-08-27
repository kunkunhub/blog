from spwb import app, cache
from spwb.models import Article
from flask import render_template, abort, request, redirect, flash


@app.route('/', defaults={'page': 1})
@cache.memoize()
def index(page):        #主页
    l = []
    pg = request.args.get('page', 1, type=int)
    pageination = Article.query.paginate(pg, per_page=20)
    if pg<0 or pg>pageination.pages:
        pg = 1
    
    for i in pageination.items:
        l.append((i.id,  i.title, i.describe))
    return render_template("index.html", arts=l, end=pageination.pages, int=int)


@app.route('/about')
@cache.cached()
def about():        #关于页面
    return render_template("about.html")


@app.route('/p/<pid>')
@cache.cached()
def p(pid):
    """
    文章的访问
    """
    pdat = Article.query.get(pid)
    if pdat == None:
        # 如果没找到
        abort(404)
    return render_template("blog/blog.html", title=pdat.title, content=pdat.content)
