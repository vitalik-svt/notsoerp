FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip3 install -r requirements.txt
RUN apt update && apt install lsof
COPY . /usr/src/app/