# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster
WORKDIR /app

COPY . /app

COPY scores.txt /scores.txt

RUN pip install -r requirements.txt

CMD [ "python", "MainScores.py" ]