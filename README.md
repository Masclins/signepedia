# Ensignepedia
Dicionari Català - LSC

## Objectiu
Crear un diccionari col·laboratiu gratuït Català - LSC accessible des de navegador i aplicació mòbil.
Entenem aquesta eina com un suport a l'aprenentatge de la LSC, no com un metodologia en si mateixa.

## Ús (Linux)
Ara per ara l'ús de l'aplicació només està testejat des de Linux.

Donat que haurem de crear un servidor local, cal instalar algunes coses.

Pel backend:
Python3 i els paquets:
* Flask
* flask-cors
* requests

Pel frontend:
* Node.js

Des del `backend/` cal mantenir executat `FLASK_APP=api.py python3 -m flask run`

Des del `frontend/` cal mantenir executat `node main.js`

L'accés a la web es fa posant `localhost:8080` al navegador.
