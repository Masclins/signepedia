# Contribuir
El funcionament del projecte es basa en crear *Issues* i fer *Pull-requests* que els solucionin.

## Nou Vocabulari
### Videos gravats
Els vídeos s'haurien de gravar amb bona llum, ben enfocats, amb fons llis, roba llisa i fosca i sense àudio.

Els vídeos gravats hauran de desar-se, en format `.mp4` a la carpeta `frontend/public/videos`. L'arxiu ha de tenir un nom únic, (a poder ser) com la paraula gravada en minúscules.

### Entrada al diccionari
El vocabulari ha d'estar tot present a `backend/diccionari.csv`. Per afegiri-hi una nova paraula caldrà fer-ho en una nova línea. Els camps del `.csv` estan a la primera línea: `"paraula","url","autor","alternatives"`. Tots els camps han de ser presents, però poden estar buits (indicat simplement amb `""`). Només els noms pròpis haurien d'estar amb la primera en majúscules.

La paraula es mostrarà quan es cerqui el que hi ha al camp `"paraula"`. Es poden fer diverses entrades si volem que surti per diferents cerques.

Si volem que al cercar una paraula es mostrin altres propostes (o alternatives) s'ha de reflectir al camp `"alternatives"`. En aquest camp ha d'haver-hi totes les entrades que volem proposar a l'usuari separades per un `|`. Pot haver-hi entrades amb només `"paraula"` i  `"alternativa"`, quan és necessàri especificar (veure l'exemple de *rosa*).

Exemples d'entrada:
* Paraula *exemple*, en el repositori (carpeta `frontend/public/videos`), gravat per *Masclins*:
`"exemple","videos/exemple.mp4","Masclins",""`
* Paraula *rosa*, referint-se a la flor, en una web en format `.wav`, gravat per *Pepito*. Volem que *rosa* ens la proposi:
`"rosa (flor)","http://webdelpepito.com/rosaLSC.wav","Pepito"`
`"rosa","","","","rosa (flor)|rosa (color)"` (assumint que també existeix una entrada per *rosa (color)*.
* Paraula *cogombre*, a YouTube, de l'usuari *LSCyoutuber*, que proposi *cogombret* (ha d'estar també registrada!):
`"cogombre","http://www.youtube.com/embed/c06oM8r3","LSCyoutuber","cogombret"`

## Issues
Una *issue* ha d'exposar un problema específic.

Totes les *issues* que es creïn han de començar amb un verb en infinitiu que descrigui la principal acció a prendre per solucionar el problema. L'excepció d'això són les *issues* creades per reportar un *bug* (error de l'aplicació), que hauràn de començar amb *Bug:*

En el cos de la *issue* ha d'haver-hi:
- Descripció clara i concisa del problema.
- Descripció clara i concisa del comportament destijat.
- En el cas dels *bugs*: passos a seguir per reproduir-lo.
- Propostes per a solucionar la *issue*, explicant de manera clara i concisa què s'ha considerat i descartat i perquè.

Per tal d'evitar que més d'una persona estigui treballant en sol·lucionar el mateix problema, caldrà assignar-se aquelles *issues* en que un estigui treballant. Es prega no assignar-se múltiples *issues* alhora.

## Pull-requests
Qualsevol *pull-request* hauria de resoldre una *issue* existent. En el cos de la *pull-request* ha d'apareixer `resolves #X`, substituint la *X* pel número de la *issue* que resol.

# Desenvolupament
Per qualsevol canvi o contribució de desenvolupament, s'espera el següent de tu:

1. Anuncia dins d'una *issue* que vols assignar-te-la (o obre-la tu).
2. No t'assignis més d'una *issue* a l'hora.
3. Dissenya tests unitaris per la teva *issue*.
4. Fes que el codi passi els tests unitaris.
5. Repeteix 3 i 4 fins que la *issue* estigui solucionada.
6. Fes una *pull-request* i demana (o espera) una *review* d'algún col·laborador.
7. Si calen canvis, torna al 3.

## Tests unitaris

### Backend
`docker-compose run backend python3 -m unittest discover`

### Frontend
`docker-compose run frontend npm test`

## Scripts
A `scripts/` hi ha alguns scripts per actualitzar `backend/diccionari.csv` i `paraules_pendents.txt`. Tot i que només cal executar-les molt de tant en tant, els incloc per simplicitat.
