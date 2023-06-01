FROM python:3.9-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /app

WORKDIR /app

COPY requirements.txt /app

RUN pip3 install -r /app/requirements.txt --no-cache-dir

RUN apt-get update

RUN apt install python3-pip libpango-1.0-0 libpangoft2-1.0-0 libjpeg-dev libopenjp2-7-dev libffi-dev -y

# Install Certbot
# RUN apt-get update && apt-get install -y certbot
# Generate SSL certificate using Certbot
# RUN certbot certonly --standalone --agree-tos --email shaldykin@gmail.com -d steelconstructor.ddns.net

COPY . /app

WORKDIR /app

# CMD ["gunicorn", "steel_oop.wsgi:application", "--bind", "0.0.0.0:8000"] 