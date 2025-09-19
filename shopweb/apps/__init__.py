from flask import Flask
import settings
from apps.order.view import order_bp
from apps.shopcar.view import shop_bp
from apps.user.view import user_bp
from exts import db,bt
from apps.product.view import pro_bp
def create_app():
    app=Flask(__name__,template_folder='../templates',static_folder='../static')
    app.config.from_object(settings.Config)
    app.register_blueprint(user_bp) #至关重要，将蓝图和app进行关联（蓝图的注册）
    app.register_blueprint(order_bp)
    app.register_blueprint(pro_bp)
    app.register_blueprint(shop_bp)
    db.init_app(app)   #将app和db建立关联
    bt.init_app(app)
    return app



