# Contribuir
El funcionament del projecte es basa en crear *Issues* i fer *Pull-requests* que els solucionin.

## Videos gravats
Els vídeos gravats hauran de desar-se, en format `.mp4` a la carpeta `frontend/public/videos`. L'arxiu ha de dir-se com la paraula gravada en minúscules.

## Vocabulari
El vocabulari ha d'estar tot present a `backend/diccionari.csv`. Per afegiri-hi una nova paraula caldrà fer-ho en una nova línea. Els camps del `.csv` estan a la primera línea: `"paraula","url","origen","autor","nota"`. Tots els camps han de ser presents, però poden estar buits (indicat simplement amb `""`).
Exemples d'entrada:
* Paraula *exemple*, en el repositori (carpeta `frontend/public/videos`), gravat per *Masclins*:
`"exemple","videos/exemple.mp4","","Masclins",""`
* Paraula *rosa*, referint-se a la flor, en una web en format `.wav`, gravat per *Pepito*:
`"rosa","http://webdelpepito.com/rosaLSC.wav","","Pepito","Flor"`
* Paraula *cogombre*, a YouTube, de l'usuari *LSCyoutuber*:
`"cogombre","http://www.youtube.com/embed/c06oM8r3","youtube","LSCyoutuber",""`

## Issues
Totes les *issues* que es creïn hauràn de començar amb un verb en infinitiu que descrigui la principal acció a prendre per solucionar un problema. El problema haurà d'estar explicat en el cos de l'*issue*.

Per tal d'evitar que més d'una persona estigui treballant en sol·lucionar el mateix problema, caldrà assignar-se aquelles *issues* en que un estigui treballant. Es prega no assignar-se múltiples *issues* alhora.

## Pull-requests
Qualsevol *pull-request* hauria de resoldre una *issue* existent. En el cos de la *pull-request* ha d'apareixer `resolves #X`, substituint la *X* pel número de la *issue* que resol.

## Desenvolupament

### Tests unitaris
A `backend/` cal executar la comanda `python3 -m unittest discover` (mentre es té el docker-compose actiu).

### Scripts R
A `scripts_R/` hi ha alguns (ara per ara un de sol) scripts per modificar `backend/diccionari.csv`. La intenció s fer-lo servir per ordenar el diccionari alfabèticament i, si calgus, aplicar-hi altres modificacions que fossin necessàries.
No és necessari fer-lo servir per al desenvolupament.
