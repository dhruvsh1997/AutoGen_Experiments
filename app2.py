from distutils.log import debug
from flask import Flask,redirect,url_for

app=Flask(__name__)

#decorator
@app.route('/')
def welcome():
    return "<html><Body><center><h1>Welcome to OE Number Checker.</h1></center></Body></Html>"

@app.route('/odd/<int:num>')
def odd(num):
    return "number is Odd :"+str(num)

@app.route('/even/<int:num>')
def even(num):
    return "number is Even :"+str(num)

@app.route('/OE/<int:val>')
def OE(val):
    result=""
    if val%2==0:
        result="even"
    else:
        result="odd"
    return redirect(url_for(result,num=val))

if __name__=='__main__':
    app.run(debug=True)
