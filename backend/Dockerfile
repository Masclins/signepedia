FROM python:3.4-alpine
LABEL maintainer="signepedia@gmail.com"

WORKDIR /usr/src/app

RUN pip3 install requests==2.18.4
RUN pip3 install Flask==0.12.2 && pip3 install flask-cors==3.0.3

CMD FLASK_APP=src/api.py python3 -m flask run --host=0.0.0.0
