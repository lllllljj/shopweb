import os
class Config:
    DEBUG=True
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:123AAaaa%%@192.168.10.102:3306/shopweb"
    BASE_DIR=os.path.dirname(os.path.abspath(__file__))#获取项目的根目录
    STATIC_DIR=os.path.join(BASE_DIR,'static')
    IMAGE=os.path.join(STATIC_DIR,'images')
    UPLOAD_DIR=os.path.join(IMAGE,'upload')
    # secret_key
    SECRET_KEY="sdfsewrtewrsdqwe"

