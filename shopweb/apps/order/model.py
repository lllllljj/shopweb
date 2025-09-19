from exts import db
class Order(db.Model):
    order_number=db.Column(db.String(10), primary_key=True)
    c_name =db.Column(db.String(15),nullable=False)
    sum = db.Column(db.String(15),nullable=False)
    pay_fangshi =db.Column(db.String(15),nullable=False)
    pay_address = db.Column(db.String(50))
    pay_email = db.Column(db.String(30))
    o_time = db.Column(db.String(20))

class Order_detail(db.Model):
    order_number = db.Column(db.String(10), primary_key=True)
    pid=db.Column(db.String(10),primary_key=True)
    price=db.Column(db.Float)
    pnum1 = db.Column(db.Integer)