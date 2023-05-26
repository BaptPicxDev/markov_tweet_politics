FROM python:3.9

RUN apt-get update

COPY src/ /src

COPY main.py .

COPY requirements.txt .

RUN pip3 install -r requirements.txt

RUN python3 main.py --api
