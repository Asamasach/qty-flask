#!/usr/bin/python
#======================================================================================
#---------Import modules like datetime/flask(web-microservice)/redis(in mem db)--------
from flask import Flask
from flask import render_template
from datetime import datetime
import redis
import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode

r=redis.Redis()
class Redis(object):
    def __init__(self, host='redis', port=6379, db=0, password=None, socket_timeout=None):
        return
app = Flask(__name__)
a=0

@app.route('/')

def qty(qty=None):

    routine()
    

    return render_template('index.html', qty=a)


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
    connection = mysql.connector.connect(host='mysql', database='webview', user='app', password='123456')
    if connection.is_connected():
        my_sql_insert_query = """INSERT INTO webview (date_stamp, quantity, time, CID) VALUES (%s, %s, %s, %s)"""
        records_to_insert = [(str(datetime.now()), a, str(datetime.now()), '1')]
        cursor = connection.cursor()
        cursor.executemany(my_sql_insert_query, records_to_insert)
        connection.commit()
        print(cursor.rowcount, "Record inserted successfully into webview table")
    return a
@app.route('/result')
def result_day(qty_day=None):
    connection = mysql.connector.connect(host='mysql', database='webview', user='app', password='123456')
    if connection.is_connected():
        cursor=connection.cursor()
        # my_sql_select_query = """ SELECT * FROM webview WHERE date_stamp >= %s AND date_stamp <= %s """
        # my_sql_select_query = """ SELECT * FROM webview"""
        my_sql_select_query = """ SELECT * FROM webview WHERE date_stamp LIKE %s """
        t1=str(datetime.now())[0:10]

        records_to_get = [(t1+'%')]
        # records_to_get = [(str(datetime.now())[0:9]+'%')]
        print(records_to_get)
        cursor.execute(my_sql_select_query, records_to_get)
        result_day=len(cursor.fetchall())

        t1=str(datetime.now())[0:8]
        records_to_get = [(t1+'%')]
        # records_to_get = [(str(datetime.now())[0:9]+'%')]
        print(records_to_get)
        cursor.execute(my_sql_select_query, records_to_get)
        result_month=len(cursor.fetchall())

        t1 = str(datetime.now())[0:5]
        records_to_get = [(t1+'%')]
        # records_to_get = [(str(datetime.now())[0:9]+'%')]
        print(records_to_get)
        cursor.execute(my_sql_select_query, records_to_get)
        result_year=len(cursor.fetchall())

        return render_template('index1.html', qty_day=result_day, qty_month=result_month, qty_year=result_year)
