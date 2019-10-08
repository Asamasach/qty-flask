from flask import Flask
from flask import render_template
from datetime import datetime
#test

app = Flask(__name__)
a=0
@app.route('/')

def qty(qty=None):
    incr()
    return render_template('index.html', qty = a)
@app.route('/add')
def db_api():
    incr()
    return {
            "qty": str(a),
            "time": str(datetime.now()),
            "CID": "1"
            }
@app.route('/time')
def timeShow():
    time = datetime.now()
    return str(time)
    return "hello this is a test for DE-104"
def incr():
    global a
    a+=1
    return a


