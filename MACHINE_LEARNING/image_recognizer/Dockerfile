FROM python:3.8-slim

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update -y
RUN apt-get -y install build-essential
RUN apt -y install python3-dev libpq-dev
RUN apt-get -y install ffmpeg libsm6 libxext6  -y

RUN pip install --upgrade pip

COPY ./requeriments.txt .

RUN pip install -r requeriments.txt

COPY . .

EXPOSE 8000
