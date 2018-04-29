# Contribuir
El funcionament del projecte es basa en crear *Issues* i fer *Pull-requests* que els solucionin.

## Vocabulari
El vocabulari ha d'estar tot present a `backend/diccionari.csv`. Per afegiri-hi una nova paraula caldrà fer-ho en una nova línea, de la seguent manera, segons on estigui allotjat el video.
* Si és al repositori (carpeta `backend/videos`): `"paraula_en_minúscules","../backend/videos/nom_del_video","","nom_de_l'autor"`
* Si és a la xarxa, i en format de video: `"paraula_en_minúscules","url", "","nom_de_l'autor"`
* Si és a youtube: `"paraula_en_minúscules","url_d'incersió", "youtube", "nom_de_l'autor"`. La url d'incersió és del tipus `http://www.youtube.com/embed/` seguit del codi del video.

### Issues
Totes les *issues* que es creïn hauràn de començar amb un verb en infinitiu que descrigui la principal acció a prendre per solucionar un problema. El problema haurà d'estar explicat en el cos de l'*issue*.

Per tal d'evitar que més d'una persona estigui treballant en sol·lucionar el mateix problema, caldrà assignar-se aquelles *issues* en que un estigui treballant. Es prega no assignar-se múltiples *issues* alhora.

## Pull-requests
Qualsevol *pull-request* hauria de resoldre una *issue* existent. En el cos de la *pull-request* ha d'apareixer `resolves #X`, substituint la *X* pel número de la *issue* que resol.

## Desenvolupament
El desenvolupament del *backend* és en Python3. A més cal instalar els paquets:
* Flask
* flask-cors

### Tests unitaris
Els canvis de desenvolupament hauràn d'anar acompanyats de tests unitaris per a cadascuna de les funcions (o com a mínim les importants).
Per executar els tests, a `backend/` cal executar la comanda `python3 -m unittest discover`

## Ús (Linux)
Des del `backend/` cal mantenir executat `FLASK_APP=api.py python3 -m flask run`

La web es troba a `frontend/main.html`
