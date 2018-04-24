import os.path
from flask import Flask
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

def paraula_existeix(paraula):
    return os.path.isfile("videos/" + paraula + ".mp4")

@app.route('/diccionari/<string:paraula>', methods=["GET"])
def url(paraula):
    if paraula_existeix(paraula):
        return "../backend/videos/" + paraula + ".mp4"
    else:
        return "SenseResultat"
