FROM python:3.12-alpine

WORKDIR app/

COPY . .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ENV PYTHONUNBUFFERED=1
