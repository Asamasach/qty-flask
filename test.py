#!/usr/bin/python
#======================================================================================
#---------Import modules like datetime/flask(web-microservice)/redis(in mem db)--------
from flask import Flask
from flask import render_template
from datetime import datetime
import redis
import mysql.connector
from mysql.connector import Error

r=redis.Redis()
class Redis(object):
    def __init__(self, host='localhost', port=6379, db=0, password=None, socket_timeout=None):
        return
app = Flask(__name__)
a=0
@app.route('/')

def qty(qty=None):
    routine()
    return render_template('index.html', qty = a)
    try:
        connection = mysql.connector.connect(host='localhost',
                                         database='mehdi',
                                         user='mehdi',
                                         password='1')

        mySql_insert_query = """INSERT INTO mehdi (timestamp, CID , qty)
                               VALUES (%s, %s, %s) """

        records_to_insert = [(str(datetime.now()), '1', a )]

        cursor = connection.cursor()
        cursor.executemany(mySql_insert_query, records_to_insert)
        connection.commit()
        print(cursor.rowcount, "Record inserted successfully into mehdi table")

    except mysql.connector.Error as error:
        print("Failed to insert record into MySQL table {}".format(error))

    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")



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
@app.route('/time')
def timeShow():
    time = datetime.now()
    return str(time)
@app.route('/redis')
def redisShow():
    return r.get("qty")
def routine():
    global a
    a+=1
    r.mset(db_api())
    print(r.get("qty"))
    return a


