from exts import db
from datetime import datetime
class User(db.Model):
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    username=db.Column(db.String(15),nullable=False)
    password = db.Column(db.String(15), nullable=False)
    phone=db.Column(db.String(11),unique=True)
    rdatetime=db.Column(db.DateTime,default=datetime.now)
class User1(db.Model):  #创建的模型类
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    username=db.Column(db.String(20),nullable=False)
    password=db.Column(db.String(20),nullable=False)
    phone=db.Column(db.String(11),unique=True)