from flask import Flask
from flask import request

app = Flask(__name__)


#http://127.0.0.1:5000/hello?name=ok
@app.route('/hello')
def hello():
    print(request.args) # 接收连接请求
    return 'hello world'


#http://127.0.0.1:5000/xxxxx?name=ok
@app.route('/xxxxx')
def xxxxx():
    print(request.args.get("name")) # 接收连接请求
    return 'xxxxx'



if __name__ == '__main__':
    app.run()