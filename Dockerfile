FROM python:3.9-slim

RUN mkdir /app

COPY requirements.txt /app

RUN pip3 install -r /app/requirements.txt --no-cache-dir

RUN apt-get update

RUN apt install python3-pip libpango-1.0-0 libpangoft2-1.0-0 libjpeg-dev libopenjp2-7-dev libffi-dev -y

COPY steel_oop/ /app

WORKDIR /app

CMD ["gunicorn", "steel_oop.wsgi:application", "--bind", "0:8000"] 