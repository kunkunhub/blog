from spwb import app
from flask import render_template
@app.route('/')
def index():        #主页
    return render_template("index.html")

@app.route('/about')
def about():        #关于页面
    return render_template("about.html")