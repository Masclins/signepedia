# Signepedia [![Codacy Badge](https://api.codacy.com/project/badge/Grade/5bf1e9d692414d78be322f17841778f0)](https://app.codacy.com/app/masclins/signepedia?utm_source=github.com&utm_medium=referral&utm_content=Masclins/signepedia&utm_campaign=badger) [![CodeFactor](https://www.codefactor.io/repository/github/masclins/signepedia/badge)](https://www.codefactor.io/repository/github/masclins/signepedia)
Dicionari cooperatiu i gratuït de català - Llengua de Signes Catalana (LSC).

## Objectiu
Crear un diccionari col·laboratiu gratuït Català - LSC accessible des de navegador i aplicació mòbil.

Estudiant LSC hem observat que resulta manquen plataformes que continguin una quantitat suficientment gran de vocabulari com per poder ser un diccionari de referència. La intenció és recollir el que poguem i, sobretot, crear una plataforma on sigui fàcil i còmode, tant consultar el vocabulari com penjar-hi nous vídeos.

Entenem aquesta eina com un suport a l'aprenentatge de la LSC, no com un metodologia en si mateixa.

## Col·laborar
Qualsevol comentari a les [Issues](https://github.com/Masclins/signepedia/issues?q=is%3Aissue+is%3Aopen+label%3Adiscussi%C3%B3) amb l'etiqueta *discussió* serà molt ben rebut i d'ajuda pel projecte.

Per una col·laboració més activa es recomana llegir el document [`docs/CONTRIBUTING.md`](https://github.com/Masclins/signepedia/blob/nou-csv/docs/CONTRIBUTING.md).

## Instal·lació
Cal instal·lar [Docker](https://store.docker.com/search?type=edition&offering=community) i clonar el repositori (`git clone https://github.com/Masclins/signepedia`).

## Ús
Cal tenir una terminal executant `docker-compose up --build` des de la carpeta del projecte.
L'aplicació és accessible des del navegador, a `localhost:8080`.

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
