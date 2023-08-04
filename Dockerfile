FROM python:3.9

COPY MLT .

RUN pip install -U pip
RUN pip install -r requirements.txt
