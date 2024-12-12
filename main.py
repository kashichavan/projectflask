from flask import Flask

app=Flask(__name__)

@app.route('/home/')
def index():
    return "Hello,olflfllrld!"

@app.route('/login/')
def login():
    return "Login Page"

if __name__=='__main__':
    app.run(host='127.0.0.1',port=6000,debug=True)