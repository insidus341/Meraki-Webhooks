FROM python:3.9.2-buster

RUN apt-get update && apt install python3-pip -y

RUN pip3 install -r requirements.txt

COPY . /app

WORKDIR /app

CMD  ["app.py"]

ENTRYPOINT ["python3"]