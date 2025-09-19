from exts import db
class Product(db.Model):
    pid=db.Column(db.String(10),primary_key=True)
    pname=db.Column(db.String(20),nullable=False)
    ptype=db.Column(db.String(20),nullable=False)
    pnum=db.Column(db.Integer)
    price=db.Column(db.Float)
    pimage=db.Column(db.String(50))