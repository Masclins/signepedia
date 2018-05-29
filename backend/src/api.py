from src.dictionary import signepedia 
from src.dictionary import counter
from src import db
from src import register
from src import unvalidated
import json
from flask import Flask
from flask import jsonify
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

mod_password = open("mod_password", "r").readline().strip("\n")

@app.route("/dictionary/<string:word>", methods=["GET"])
def search_word(word):
    cnx = db.connect()
    register.register_search(word, cnx)
    entry = signepedia.get_entry(word, cnx)
    cnx.close()
    return jsonify(entry)

@app.route("/counter", methods=["GET"])
def count_videoIds():
    cnx = db.connect()
    number = str(counter.videoIds(cnx))
    cnx.close()
    return number

@app.route("/new_entry/<string:newEntry>", methods=["GET"])
def insert_new_entry(newEntry):
    cnx = db.connect()
    answer = unvalidated.insert(json.loads(newEntry), cnx)
    cnx.close()
    return answer

@app.route("/validate/<string:validEntry>", methods=["GET"])
def validate_entry(validEntry):
    validEntry = json.loads(validEntry)
    if validEntry["password"] == mod_password:
        cnx = db.connect()
        answer = unvalidated.validate(validEntry, cnx)
        cnx.close()
        return answer
    return "wrong_password"

@app.route("/get_unvalidated", methods=["GET"])
def get_unvalidated():
    cnx = db.connect()
    answer = jsonify(unvalidated.get_unvalidated(cnx))
    cnx.close()
    return answer
