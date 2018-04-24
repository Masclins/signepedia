# Contribuir
El funcionament del projecte es basa en crear *Issues* i fer *Pull-requests* que els solucionin.

## Vocabulari
Tot el vocabulari que afegim (de moment) ha de seguir el següent format:
* El nom de l'arxiu serà la paraula definida.
* Tot serà en minúscules i sense accents.
* El format serà mp4.

## Issues
Totes les *issues* que es creïn hauràn de començar amb un verb en infinitiu que descrigui la principal acció a prendre per solucionar un problema. El problema haurà d'estar explicat en el cos de l'*issue*.

Per tal d'evitar que més d'una persona estigui treballant en sol·lucionar el mateix problema, caldrà assignar-se aquelles *issues* en que un estigui treballant. Es prega no assignar-se múltiples *issues* alhora.

## Pull-requests
Qualsevol *pull-request* hauria de resoldre una *issue* existent. En el cos de la *pull-request* ha d'apareixer `resolves #X`, substituint la *X* pel número de la *issue* que resol.

## Desenvolupament
El desenvolupament del *backend* és en Python3. A més cal instalar els paquets:
* Flask
* flask-cors

### Tests unitaris
Els canvis de desenvolupament hauràn d'anar acompanyats de tests unitaris per a cadascuna de les funcions.

## Ús (Linux)
Des del `backend/` cal mantenir executat `FLASK_APP=buscador.py python3 -m flask run`

La web es troba a `frontend/main.html`
