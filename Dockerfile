FROM python:3.9.2-buster

RUN apt-get update && apt install python3-pip -y

COPY requirements.txt /app/requirements.txt

RUN pip3 install -r /app/requirements.txt

COPY . /app

WORKDIR /app

CMD  ["app.py"]

ENTRYPOINT ["python3"]