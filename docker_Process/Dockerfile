FROM ubuntu:14.04

RUN apt-get -yqq update
RUN apt-get install -yqq python3

COPY /app ./app


CMD python3 app/test.py
