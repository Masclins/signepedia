FROM node:9.11.1-alpine
LABEL maintainer="signepedia@gmail.com"

WORKDIR /usr/src/app
COPY . /usr/src/app/

RUN apk add git --no-cache
RUN npm install --quiet

CMD node src/main.js
