FROM python:3.4-alpine
LABEL maintainer="signepedia@gmail.com"

WORKDIR /usr/src/app

RUN apk add git --no-cache
RUN pip3 install requests==2.18.4
RUN pip3 install mysql-connector-python==8.0.11
RUN pip3 install Flask==0.12.2 && pip3 install flask-cors==3.0.3
RUN pip3 install coverage==4.5.1 && pip3 install codacy-coverage==1.3.11

CMD FLASK_APP=api.py python3 -m flask run --host=0.0.0.0
