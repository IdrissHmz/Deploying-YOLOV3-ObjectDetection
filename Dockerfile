FROM ubuntu:20.04


WORKDIR /app

ENV PYTHONUNBUFFERED=1
RUN apt-get update && apt-get install python3.7 && apt-get install python3-pip -y && apt-get install -y netcat
RUN pip3 install --no-cache --upgrade pip setuptools

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

RUN chmod +x entrypoint.sh

CMD [ "sh", "./entrypoint.sh"]