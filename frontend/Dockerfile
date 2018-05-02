FROM node:9.11.1-alpine
WORKDIR /usr/src/app
COPY package.json /usr/src/app/
RUN npm install --quiet
COPY . /usr/src/app
CMD node main.js
