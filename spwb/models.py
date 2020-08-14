# 数据库
# 完善中...
import sys
import os
from spwb import db

class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(60))
    content = db.Column(db.Text)