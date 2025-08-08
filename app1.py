from distutils.log import debug
from flask import Flask
#WSGI App
app=Flask(__name__)

#when we use default Static url
@app.route('/')
def welcome():
    return "Welcome to the State."
#when we use static url with new binding function '/city'

@app.route('/city')
def city():
    return "Welcome to the City."

if __name__=='__main__':
    app.run(debug=True)