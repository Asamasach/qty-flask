import mysql.connector
from mysql.connector import Error


def connect():
    connection = None
    try:
        connection = mysql.connector.connect(host='192.168.122.100',
                                         database='mehdi',
                                         user='mehdi',
                                         password='1')
        if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Connected to MySQL Server version ", db_Info)
            cursor = connection.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            print("Your connected to database: ", record)

    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            rint("MySQL connection is closed")

