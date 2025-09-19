from exts import db
class Shopcar(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(15), nullable=False)
    pid = db.Column(db.String(10),nullable=False)
    pnum1 = db.Column(db.Integer)