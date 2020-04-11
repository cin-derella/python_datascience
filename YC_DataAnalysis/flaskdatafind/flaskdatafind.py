from flask import Flask
from finddata import CSDNFind

app = Flask(__name__)
csdnFilePath =  '../YCdata/csdnindexsort.txt'
csdnIndexFilePath =  '../YCdata/csdnsortindexnew.txt'
csdn = CSDNFind(csdnFilePath,csdnIndexFilePath)

@app.route('/')
def hello_world():
    return 'hello world!'

@app.route('/<name>')
def get_data(name):
    return str(csdn.search2(name))


@app.route('/csdn/<name>')
def get_data1(name):
    return str(csdn.search2(name))


if __name__ == '__main__':
    app.run()
