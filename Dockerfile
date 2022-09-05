FROM ubuntu:20.04


WORKDIR /app

ENV PYTHONUNBUFFERED=1
RUN apt-get update && apt-get install -y python3.9 && apt-get install -y  python3-pip && apt-get install -y netcat
RUN pip3 install --no-cache --upgrade pip setuptools

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

RUN rm client.py
RUN rm -rf ./images

RUN chmod +x entrypoint.sh

CMD [ "sh", "./entrypoint.sh"]