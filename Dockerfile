FROM python:3.9-slim

RUN mkdir /app

COPY requirements.txt /app

RUN pip3 install -r /app/requirements.txt --no-cache-dir

COPY steel_oop/ /app

WORKDIR /app

CMD ["gunicorn", "steel_oop.wsgi:application", "--bind", "0:8000"] 