# from flask import Blueprint,render_template,request,session,redirect,jsonify
# from exts import db
# from apps.user.model import *
# from apps.product.model import Product
# user_bp=Blueprint('user',__name__)  #蓝图的实例化
#
# @user_bp.route('/index')
# def index():
#     # uid=request.cookies.get('uid',None)  #cookie的获取
#     products=Product.query.all()
#     uid=session.get('uid',None)  #session的获取
#     user=User.query.get(uid)#根据主键查找对象     模型类.query.get(主键)
#     return render_template('index.html',products=products,user=user)
# @user_bp.route('/user_login',methods=['GET','POST'])  #通过蓝图创建路由
# def user_login():
#     if request.method=='POST':
#         username=request.form.get('username')
#         password = request.form['password']
#         # users=User.query.filter(User.username=='陈宇生',User.password=='9999').all()  #返回一个列表,返回查询的所有数据
#         # if len(users)==0:
#         #     return "用户名或者密码错误"
#         # else:
#         #     return "登录成功"
#         user=User.query.filter(User.username==username,User.password==password).first()  #返回一条记录 ，返回值是一个对象
#         if user is None:
#             return "用户名或者密码错误"
#         else:
#             # resp=redirect('/index')
#             # resp.set_cookie('uid',str(user.id))  #cookie的设置
#             # return resp
#             session['uid']=user.id  #保存用户的id
#             session['uname']=user.username
#             return redirect('/index')  #redirect 路由的跳转
#     else:
#         return render_template('login.html')
#
#     # return render_template('login.html')  #渲染模板
# @user_bp.route('/user_register',methods=['GET','POST'])
# def register():
#     if request.method=='POST':   #数据的添加
#         username=request.form.get('username')
#         password=request.form['password']
#         repwd=request.form.get('repassword')
#         phone=request.form.get('phone')
#         if password==repwd:
#             user=User()   #创建对象
#             user.username=username   #对属性赋值，赋从文本框获取的值
#             user.password=password
#             user.phone=phone
#             db.session.add(user)  #将对象添加到缓存
#             db.session.commit()  #提交到数据库
#             return "注册成功"
#         else:
#             return "两次输入的密码不一致"
#
#     else:  #get请求
#         return render_template('user_register.html')
# @user_bp.route('/user_logout')
# def user_logout():
#     session.pop('uid')  #清除session
#     # session.clear()
#     return redirect('/index')
#     # response=redirect('/index')
#     # response.delete_cookie('uid')  #cookie的删除
#     # return response
# @user_bp.route('/user_show')
# def user_show():
#     users=User.query.all() #查询用户表的所有数据
#     return render_template('user_show.html',users=users)
# @user_bp.route('/user_update',methods=['GET','POST'])
# def user_update():
#     if request.method=='POST':
#         id=request.form.get('uid')
#         username=request.form.get('username')
#         password=request.form.get('pwd')
#         phone=request.form.get('phone')
#         user=User.query.get(id)  #根据主键查找对象
#         user.password=password   #修改数据
#         user.phone=phone
#         user.username=username
#         db.session.commit()    #提交到数据库
#         return redirect('/user_show')
#     else:
#         uid=request.args.get('uid') #get请求获取数据
#         user=User.query.get(uid)  #根据主键查找对象
#         return render_template('user_update.html',user=user)
# @user_bp.route('/user_del')
# def user_del():
#     id=request.args.get('uid')   #get请求获取数据
#     user=User.query.get(id)
#     db.session.delete(user)#删除对象，提交到缓存
#     db.session.commit()  #提交到数据库
#     return redirect('/user_show')
# @user_bp.route('/testwindow')
# def testwin():
#     return render_template('1.html')
# @user_bp.route('/demo',methods=['GET','POST'])
# def demo():
#     if request.method=='POST':
#         username=request.form['username']  #获取数据
#         age=request.form.get('age')
#         data={'username':username,'age':age,'code':200}
#         print(data)
#         return jsonify(data)
#     else:
#         return render_template('demo.html')
# @user_bp.route('/demo1',methods=['GET','POST'])
# def demo1():
#     if request.method=='POST':
#         num=request.form['number']
#         data={'number':num}
#         return jsonify(data)
#     else:
#         return render_template('demo1.html')
#
#
from flask import Blueprint, render_template, request, session, redirect, jsonify
from exts import db
from apps.user.model import *
from apps.product.model import Product

user_bp = Blueprint('user', __name__)

@user_bp.route('/')  # 添加根路径路由，渲染首页
def index():
    products = Product.query.all()
    uid = session.get('uid', None)
    user = User.query.get(uid) if uid else None
    return render_template('index.html', products=products, user=user)

@user_bp.route('/user_login', methods=['GET', 'POST'])
def user_login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form['password']
        user = User.query.filter(User.username == username, User.password == password).first()
        if user is None:
            return "用户名或者密码错误"
        else:
            session['uid'] = user.id
            session['uname'] = user.username
            return redirect('/index')
    else:
        return render_template('login.html')

@user_bp.route('/user_register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form['password']
        repwd = request.form.get('repassword')
        phone = request.form.get('phone')
        if password == repwd:
            user = User()
            user.username = username
            user.password = password
            user.phone = phone
            db.session.add(user)
            db.session.commit()
            return "注册成功"
        else:
            return "两次输入的密码不一致"
    else:
        return render_template('user_register.html')

@user_bp.route('/user_logout')
def user_logout():
    session.pop('uid')
    return redirect('/index')

@user_bp.route('/user_show')
def user_show():
    users = User.query.all()
    return render_template('user_show.html', users=users)

@user_bp.route('/user_update', methods=['GET', 'POST'])
def user_update():
    if request.method == 'POST':
        id = request.form.get('uid')
        username = request.form.get('username')
        password = request.form.get('pwd')
        phone = request.form.get('phone')
        user = User.query.get(id)
        user.password = password
        user.phone = phone
        user.username = username
        db.session.commit()
        return redirect('/user_show')
    else:
        uid = request.args.get('uid')
        user = User.query.get(uid)
        return render_template('user_update.html', user=user)

@user_bp.route('/user_del')
def user_del():
    id = request.args.get('uid')
    user = User.query.get(id)
    db.session.delete(user)
    db.session.commit()
    return redirect('/user_show')

@user_bp.route('/testwindow')
def testwin():
    return render_template('1.html')

@user_bp.route('/demo', methods=['GET', 'POST'])
def demo():
    if request.method == 'POST':
        username = request.form['username']
        age = request.form.get('age')
        data = {'username': username, 'age': age, 'code': 200}
        print(data)
        return jsonify(data)
    else:
        return render_template('demo.html')

@user_bp.route('/demo1', methods=['GET', 'POST'])
def demo1():
    if request.method == 'POST':
        num = request.form['number']
        data = {'number': num}
        return jsonify(data)
    else:
        return render_template('demo1.html')