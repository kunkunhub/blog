from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_debugtoolbar import DebugToolbarExtension
from flask_caching import Cache

app = Flask(__name__)
app.config.from_pyfile('settings.py')   # 从settings.py中导入设置
# 去除jinja模板中的空白行
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True

db = SQLAlchemy(app)
toolbar = DebugToolbarExtension(app)
cache = Cache(app)

from spwb import views, errors, commands


