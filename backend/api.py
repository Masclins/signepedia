from dictionary import main
from dictionary import alter
from dictionary import counter
from dictionary import search
import db
import register
import users
import json
from flask import Flask
from flask import jsonify
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

# Returns the basic information about the dictionary.
@app.route("/main", methods=["GET"])
def main_info():
    cnx = db.connect()
    cursor = cnx.cursor(dictionary=True)
    data = jsonify(dict(nVideos=counter.get_nVideos(cursor)))
    cursor.close()
    cnx.close()
    return data

# Returns the info for a word.
# That includes all entries, synonyms and correction when applies.
@app.route("/dictionary/<string:word>", methods=["GET"])
def search_word(word):
    cnx = db.connect()
    cursor = cnx.cursor(dictionary=True)
    register.searches(word, cursor)
    resp = jsonify(main.get_result(word, cursor))
    cursor.close()
    cnx.commit()
    cnx.close()
    return resp

# Returns the info for a word from a user point of view.
# That includes all entries, synonyms and correction when applies.
# Also includes any already casted vote for each entry.
@app.route("/dictionary/<string:word>/user/<int:userId>", methods=["GET"])
def search_word_user(word, userId):
    cnx = db.connect()
    cursor = cnx.cursor(dictionary=True)
    register.searches(word, cursor)
    resp = jsonify(main.get_result_user(word, userId, cursor))
    cursor.close()
    cnx.commit()
    cnx.close()
    return resp

# Adds a new entry into the dictionary
@app.route("/dictionary/<string:entry>", methods=["POST"])
def insert_new_entry(entry):
    cnx = db.connect()
    cursor = cnx.cursor(dictionary=True)
    alter.insert(json.loads(entry), cursor)
    cursor.close()
    cnx.commit()
    cnx.close()

# Return a single entry.
@app.route("/entries/<int:entryId>", methods=["GET"])
def get_entry(entryId):
    cnx = db.connect()
    cursor = cnx.cursor(dictionary=True)
    entry = jsonify(search.get_entry(entryId, cursor))
    cursor.close()
    cnx.close()
    return entry

# Edits some values of an entry
@app.route("/entries/<int:entryId>/edits/<string:edits>", methods=["PATCH"])
def edit_entry(entryId, edits):
    cnx = db.connect()
    cursor = cnx.cursor(dictionary=True)
    alter.edit_entry(entryId, json.loads(edits), cursor)
    cursor.close()
    cnx.commit()
    cnx.close()

# Deletes an entry
@app.route("/entries/<int:entryId>", methods=["DELETE"])
def delete_entry(entryId):
    cnx = db.connect()
    cursor = cnx.cursor(dictionary=True)
    alter.delete_entry(entryId, cursor)
    cursor.close()
    cnx.commit()
    cnx.close()

# Votes for an entry
@app.route("/entries/<int:entryId>/vote/<string:vote>/user/<int:userId>", methods=["POST"])
def vote_entry(entryId, vote, userId):
    cnx = db.connect()
    cursor = cnx.cursor(dictionary=True)
    vote.vote(entryId, userId, vote, cursor)
    cursor.close()
    cnx.commit()
    cnx.close()

# Registers a user
@app.route("/users/<string:newUser>", methods=["POST"])
def new_user(newUser):
    cnx = db.connect()
    cursor = cnx.cursor(dictionary=True)
    answer = users.new_user(json.loads(newUser), cursor)
    cursor.close()
    cnx.commit()
    cnx.close()
    return answer
