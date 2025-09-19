from flask import Blueprint,render_template,session,request
from apps.product.model import Product
from apps.shopcar.model import Shopcar
from sqlalchemy import and_,or_
from apps.user.model import User
from exts import db
from apps.order.model import *
import random,datetime
order_bp=Blueprint('order',__name__)
@order_bp.route('/order1',methods=['GET','POST'])
def order1():
    if request.method=='POST':
        username=session['uname']
        sum=session['sum']
        pay_fangshi=request.form.get('pay_fangshi')  #根据下拉列表框name得到选中项的value
        pay_email=request.form.get('pay_email')
        pay_address=request.form['pay_address']
        a = random.random()
        order_number = str(a)[2:12]
        o_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
        session['pay_fangshi']=pay_fangshi
        session['pay_email']=pay_email
        session['pay_address']=pay_address
        session['order_number']=order_number
        session['o_time']=o_time
        shops = db.session.query(Product, Shopcar).join(Shopcar, and_(Product.pid == Shopcar.pid,
                                                                      Shopcar.username == username)).all()
        return render_template('order/order2.html',shops=shops,sum=sum)
    else:
        username = session['uname']
        id = session['uid']
        user = User.query.get(id)
        shops = db.session.query(Product, Shopcar).join(Shopcar, and_(Product.pid == Shopcar.pid,
                                                                      Shopcar.username == username)).all()
        sum = 0
        for p, s in shops:
            sum = sum + p.price * s.pnum1
        return render_template('order/order1.html', shops=shops, sum=sum, user=user)

