import mysql.connector
import json
import os
import datetime

def connect():
    try:
        with open("private/mysql_data.json") as file_data:
            data = json.load(file_data)
    except FileNotFoundError:
        data = dict(
                user=os.environ["SIGNEPEDIA_MYSQL_USER"],
                password=os.environ["SIGNEPEDIA_MYSQL_PASSWORD"],
                host=os.environ["SIGNEPEDIA_MYSQL_HOST"],
                database=os.environ["SIGNEPEDIA_MYSQL_DATABASE"])
    cnx = mysql.connector.connect(
            user=data["user"],
            password=data["password"],
            host=data["host"],
            database=data["database"],
            use_pure=False)
    return cnx

def errorLog(func, var, err):
    cnx = connect()
    cursor = cnx.cursor(prepared=True)

    query = "INSERT INTO errors VALUES (%s, %s, %s, %s)"
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute(query, (func, var, err, now))

    cnx.commit()
    cursor.close()
    cnx.close()
