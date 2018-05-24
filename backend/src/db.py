import mysql.connector
import json
import os

def connect():
    try:
        with open("mysql_data.json") as file_data:
            data = json.load(file_data)
    except FileNotFoundError:
        data = dict(user=os.environ["SIGNEPEDIA_MYSQL_USER"], password=os.environ["SIGNEPEDIA_MYSQL_PASSWORD"], host=os.environ["SIGNEPEDIA_MYSQL_HOST"], database=os.environ["SIGNEPEDIA_MYSQL_DATABASE"])
    cnx = mysql.connector.connect(user=data["user"], password=data["password"], host=data["host"], database=data["database"], use_pure=False)
    return cnx
