from cercador import cercador 
from flask import Flask
from flask import jsonify
from flask_cors import CORS
import requests
app = Flask(__name__)
CORS(app)

@app.route('/diccionari/<string:paraula>', methods=["GET"])
def cerca_entrada(paraula):
    entrada = cercador.entrada(paraula)
    return jsonify(paraula=paraula, url=entrada[0], origen=entrada[1])
