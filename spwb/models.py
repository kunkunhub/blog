# 数据库
# 完善中...
import sys
import os
from spwb import db
from werkzeug.security import generate_password_hash, check_password_hash

class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(60))
    content = db.Column(db.Text)
    describe = db.Column(db.String(1000))

class Admin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    password = db.Column(db.String(256))

    def set_password(self, passwd):
        """
        设置密码
        """
        self.password = generate_password_hash(passwd)
    
    def validate_password(self, passwd):
        """
        检查密码
        """
        return check_password_hash(self.password, passwd)
    