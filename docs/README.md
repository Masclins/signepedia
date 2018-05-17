# [Signepedia](http://signepedia.cat) [![Codacy Badge](https://api.codacy.com/project/badge/Grade/a35eacf1879e41b7b5e5c330f37b3e22)](https://www.codacy.com/app/masclins/signepedia?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=Masclins/signepedia&amp;utm_campaign=Badge_Grade) [![Codacy Badge](https://api.codacy.com/project/badge/Coverage/a35eacf1879e41b7b5e5c330f37b3e22)](https://www.codacy.com/app/masclins/signepedia?utm_source=github.com&utm_medium=referral&utm_content=Masclins/signepedia&utm_campaign=Badge_Coverage) [![CodeFactor](https://www.codefactor.io/repository/github/masclins/signepedia/badge)](https://www.codefactor.io/repository/github/masclins/signepedia)
Dicionari cooperatiu i gratuït de català - Llengua de Signes Catalana (LSC).

## Objectiu
Crear un diccionari col·laboratiu gratuït Català - LSC accessible des de navegador i aplicació mòbil.

Estudiant LSC hem observat que resulta manquen plataformes que continguin una quantitat suficientment gran de vocabulari com per poder ser un diccionari de referència. La intenció és recollir el que poguem i, sobretot, crear una plataforma on sigui fàcil i còmode, tant consultar el vocabulari com penjar-hi nous vídeos.

Entenem aquesta eina com un suport a l'aprenentatge de la LSC, no com un metodologia en si mateixa.

## Col·laborar
Qualsevol comentari a les [Issues](https://github.com/Masclins/signepedia/issues?q=is%3Aissue+is%3Aopen+label%3Adiscussi%C3%B3) amb l'etiqueta *discussió* serà molt ben rebut i d'ajuda pel projecte.

Per una col·laboració més activa es recomana llegir el document [`docs/CONTRIBUTING.md`](https://github.com/Masclins/signepedia/blob/nou-csv/docs/CONTRIBUTING.md).

## Instal·lació
L'aplicació és accesible en l'estat de la branca `master` a http://signepedia.cat.

Per fer servir la versió en local, cal instal·lar [Docker](https://store.docker.com/search?type=edition&offering=community) i clonar el repositori (`git clone https://github.com/Masclins/signepedia`).

## Ús
Cal tenir una terminal executant `docker-compose up --build` des de la carpeta del projecte.
L'aplicació és accessible des del navegador, a `localhost`.

Per permetre la pujada de vídeos des del frontend cal crear l'arxiu `frontend/dades_correu.json`.
En aquest arxiu ha d'haver-hi:
```json
{
	"usuari": EMAIL,
	"contrasenya": CONTRASENYA
}
```

## Llicència

Copyright © 2018 Albert Masclans

Distribuït sota MIT License.
