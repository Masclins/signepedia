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

cnx = db.connect()
mod_password = open("mod_password", "r").readline().strip("\n")

@app.route("/dictionary/<string:word>", methods=["GET"])
def search_word(word):
    register.register_search(word, cnx)
    entry = signepedia.get_entry(word, cnx)
    return jsonify(entry)

@app.route("/counter", methods=["GET"])
def count_videoIds():
    return str(counter.videoIds(cnx))

@app.route("/new_entry/<string:newEntry>", methods=["GET"])
def insert_new_entry(newEntry):
    return unvalidated.insert(json.loads(newEntry), cnx)

@app.route("/validate/<string:validEntry>", methods=["GET"])
def validate_entry(validEntry):
    validEntry = json.loads(validEntry)
    if validEntry["password"] == mod_password:
        return unvalidated.validate(validEntry, cnx)
    return "wrong_password"

@app.route("/get_unvalidated", methods=["GET"])
def get_unvalidated():
    return jsonify(unvalidated.get_unvalidated(cnx))
