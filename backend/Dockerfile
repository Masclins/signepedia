FROM python:3.4-alpine
WORKDIR /usr/src/app
RUN pip3 install requests && pip3 install Flask && pip3 install flask-cors
CMD FLASK_APP=src/api.py python3 -m flask run --host=0.0.0.0
