from cercador import cercador 
from flask import Flask
from flask import jsonify
from flask_cors import CORS
import requests
app = Flask(__name__)
CORS(app)

@app.route('/diccionari/<string:paraula>', methods=["GET"])
def consulta_paraula(paraula):
    entrada = cercador.cerca_paraula(paraula)
    return jsonify(entrada)
