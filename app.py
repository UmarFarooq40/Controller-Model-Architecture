from flask import Flask,request,render_template

app=Flask(__name__)



@app.route('/home')
def home():
    return "<h1>THIS IS HOMEPAGE</h1>"
@app.route('/index')
def index():
    return render_template('index.html')


if __name__=='__main__':
    app.run(debug=True)



from controller import *