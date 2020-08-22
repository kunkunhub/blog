from spwb import app, cache
from spwb.models import Article
from flask import render_template, abort, request, redirect


@app.route('/', defaults={'page': 1})
@cache.memoize()
def index(page):        #主页
    l = []
    for i in Article.query.all():
        l.append((i.id, i.title))
    pg = request.args.get('page', 1)
    try:
        pg = int(pg)
    except ValueError:
        abort(404)
    pageination = Article.query.paginate(page, per_page=50)
    if pg<0 or pg>pageination.pages:
        abort(404)
    return render_template("index.html", arts=l, end=pageination.pages, int=int)


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
