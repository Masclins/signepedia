# Ensignepedia
Dicionari Català - LSC

## Objectiu
Crear un diccionari col·laboratiu gratuït Català - LSC accessible des de navegador i aplicació mòbil.
Entenem aquesta eina com un suport a l'aprenentatge de la LSC, no com un metodologia en si mateixa.

## Ús (Linux)
Ara per ara l'ús de l'aplicació només està testejat des de Linux.

Donat que haurem de crear un servidor local, cal tenir instalat Python3 i els paquets:
* Flask
* flask-cors

Des del `backend/` cal mantenir executat `FLASK_APP=api.py python3 -m flask run`

La web es troba a `frontend/main.html`
