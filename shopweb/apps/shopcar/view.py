from flask import Blueprint,request,session,redirect,render_template,url_for,jsonify
from exts import db
from sqlalchemy import and_,or_
from apps.product.model import Product
from apps.shopcar.model import Shopcar
from apps.user.model import User
shop_bp=Blueprint('shopcar',__name__,url_prefix='/shopcar')
@shop_bp.route('/shop_add')
def shop_add():
    pid=request.args.get('pid')  #获取商品编号
    username=session['uname']
    shopcars=Shopcar.query.all()  #查询购物车表的所有数据
    for shopcar in shopcars:
        if shopcar.pid==pid and shopcar.username==username:
            shopcar.pnum1=shopcar.pnum1+1  #数据的修改
            db.session.commit()
            return redirect('/shopcar/shop_count')

    else:
        shopcar=Shopcar()
        shopcar.username=username
        shopcar.pid=pid
        shopcar.pnum1=1
        db.session.add(shopcar)
        db.session.commit()
        return redirect('/shopcar/shop_count')
@shop_bp.route('/shop_count')
def shop_count():
    username=session['uname']
    id=session['uid']
    user=User.query.get(id)
    shops=db.session.query(Product,Shopcar).join(Shopcar,and_(Product.pid==Shopcar.pid,Shopcar.username==username)).all()
    # session['shops']=shops
    sum=0
    for p,s in shops:
        sum=sum+p.price*s.pnum1
    session['sum']=str(sum)
    return render_template('shopcar.html',shops=shops,sum=sum,user=user)
@shop_bp.route('/shop_clear')
def shop_clear():
    username = session['uname']
    Shopcar.query.filter(Shopcar.username==username).delete()  #针对查询结果进行删除
    db.session.commit()
    return redirect('/shopcar/shop_count')
@shop_bp.route('/shop_delete')
def shop_delete():
    id=request.args.get('sid')
    print(id)
    shopcar=Shopcar.query.get(id)
    db.session.delete(shopcar)
    db.session.commit()
    return redirect(url_for('shopcar.shop_count'))
@shop_bp.route('/shopcar_update',methods=['GET','POST'])
def shopcar_update():
    if request.method=='POST':
        pnum1=request.form['pnum1']
        sid=request.form['sid']
        print(pnum1)
        print(sid)
        shopcar=Shopcar.query.get(sid)
        shopcar.pnum1=pnum1
        db.session.commit()  #更新购物车的数量
        res={'success':'OK','sid':sid}
        return jsonify(res)
    else:
        return "asas"
@shop_bp.route('/pro_xq')
def pro_xq():
    pid=request.args.get('pid')
    product=Product.query.get(pid)
    return render_template('pro/pro_xq.html',product=product)


