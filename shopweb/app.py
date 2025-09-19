from apps import create_app  #导入函数
app=create_app()  #调用函数实现app的实例化
if __name__ == '__main__':
    app.run()  #运行项目
