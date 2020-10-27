FROM python:3.8

ADD requirements.txt /tmp/requirements.txt

RUN pip install --upgrade -r /tmp/requirements.txt

WORKDIR /code

ADD . /code

