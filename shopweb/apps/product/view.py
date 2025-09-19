from flask import Blueprint,render_template,request,session
from apps.product.model import Product
import os
from exts import db
from settings import Config
pro_bp=Blueprint('product',__name__)
@pro_bp.route('/pro_show')
def pro_show():  #商品的展示
    username=session['uname']
    products=Product.query.all()  #查询商品表的所有数据 ,返回的结果为列表类型
    return render_template('pro_show.html',products=products,username=username)
@pro_bp.route('/pro_add',methods=['GET','POST'])
def pro_add():
    if request.method=='POST':
        file1=request.files.get('pimage') #获取文件对象
        filename=file1.filename  #获取文件名
        file_path=os.path.join(Config.UPLOAD_DIR,filename)  #最终的路径
        file1.save(file_path)  #文件的上传
        pid=request.form.get('pid')
        pname=request.form.get('pname')
        ptype=request.form.get('ptype')
        price = float(request.form.get('price'))
        pnum = int(request.form.get('pnum'))
        pimage=os.path.join('images/upload/',filename)  #数据库要保存的图片路径
        product=Product()
        product.pid=pid
        product.pname=pname
        product.ptype=ptype
        product.price = price
        product.pnum = pnum
        product.pimage=pimage
        db.session.add(product)  #提交到缓存
        db.session.commit()  #提交到数据库
        return "上传成功"
    else:
        return render_template('pro_add.html')
@pro_bp.route('/pro_search',methods=['GET','POST'])
def pro_search():
    if request.method=='POST':
        ptype=request.form.get('ptype') #获取文本框的值
        products=Product.query.filter(Product.ptype.contains(ptype)).all()  #过滤查询  模型查询
        return render_template('index.html',products=products)
    else:
        products = Product.query.all()
        return render_template('index.html', products=products)
