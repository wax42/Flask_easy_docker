FROM ubuntu:14.04

RUN apt-get -yqq update
RUN apt-get install -yqq python3
RUN apt-get install -yqq python3-pip
RUN pip3 install Flask

COPY /app ./app

EXPOSE 8080

CMD python3 app/flask_api.py
