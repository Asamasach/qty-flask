#!/usr/bin/python
#======================================================================================
#---------Import modules like datetime/flask(web-microservice)/redis(in mem db)--------

from flask import Flask, jsonify, request
from flask import render_template
from datetime import datetime
import redis

import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode




app = Flask(__name__)
a=0

r=redis.Redis(host='redis', port=6379 , db=0, password=None, socket_timeout=None)
# class Redis(object):
#     def __init__(self, host='redis', port=6379, db=0, password=None, socket_timeout=None):
#         return

# r=redis.Redis( host='redis', port=6379 )


@app.route('/json')
def db_api():
    return {
            str(datetime.now()): str({
                "quantity": str(a),
                "time": str(datetime.now()),
                "CID": "1"
                }),
            "qty" : str(a)
            }

@app.route('/<uuid>', methods=['GET', 'POST'])
def add_message(uuid):
    content = request.json
  #  print(content['mytext'])
    return jsonify({"uuid":uuid})

def routine():
    global a
    a+=1
    r.mset(db_api())
    print(r.get("qty"))
    connection = mysql.connector.connect(host='my_sql', port='3306', database='webview', user='root', password='')
    if connection.is_connected():
         my_sql_insert_query = """INSERT INTO webview (date_stamp, quantity, time, CID) VALUES (%s, %s, %s, %s)"""
         records_to_insert = [(str(datetime.now()), a, str(datetime.now()), '1')]
         cursor = connection.cursor()
         cursor.executemany(my_sql_insert_query, records_to_insert)
         connection.commit()
         print(cursor.rowcount, "Record inserted successfully into webview table")
    return a



@app.route('/')
def qty(qty=None):
    routine()
    return render_template('index.html', qty=a)


@app.route('/time')
def timeShow():
    time = datetime.now()
    return str(time)

@app.route('/my_form', methods=['POST'])
def my_form():
    form_input = request.form['comment_content']
    # Now that get value back to server can send it to a DB(use Flask-SQLAlchemy)
    return(form_input)

@app.route('/show_form')
def index_form():
    return render_template('index_form.html')

@app.route('/manage_game', methods=['POST'])
def manage_game():
    start = request.form['action'] == 'Start'
    game_id = request.form['game_id']

    if start:
        start_game(game_id)
    else:
        stop_game(game_id)

    return redirect(url_for('index'))

@app.route('/save', methods=['POST'])
def save():
    if request.method == 'POST':
        clean_and_validate_the_data() # some functional code you need to handle POST data
        save_the_data() # some functional code to save our data 
    return redirect(url_for("index"))

@app.route('/test')
def hello():
    name = request.args['name']
    return """
        <html><body>
            <h1>Hello, {0}!</h1>
            The time is {1}.
        </body></html>
        """.format(
            name, str(datetime.now()))

@app.route('/new_form', methods=['GET', 'POST'])
def new_album():
    """
    Add a new form
    """
    form = AlbumForm(request.form)
    return render_template('index_form.html', form=form)

@app.route('/redis')
def redisShow():
    return r.get("qty")
@app.route('/result')
def result_day(qty_day=None):
    connection = mysql.connector.connect(host='my_sql', database='webview', user='root', password='')
    if connection.is_connected():
        cursor=connection.cursor()
        my_sql_select_query = """ SELECT * FROM webview WHERE date_stamp LIKE %s """
        t1=str(datetime.now())[0:10]

        records_to_get = [(t1+'%')]
        print(records_to_get)
        cursor.execute(my_sql_select_query, records_to_get)
        result_day=len(cursor.fetchall())

        t1=str(datetime.now())[0:8]
        records_to_get = [(t1+'%')]
        print(records_to_get)
        cursor.execute(my_sql_select_query, records_to_get)
        result_month=len(cursor.fetchall())

        t1 = str(datetime.now())[0:5]
        records_to_get = [(t1+'%')]
        print(records_to_get)
        cursor.execute(my_sql_select_query, records_to_get)
        result_year=len(cursor.fetchall())
    return render_template('index1.html', qty_day=result_day, qty_month=result_month, qty_year=result_year)

if __name__=="__main__":
    app.run(host="0.0.0.0", debug=True)
