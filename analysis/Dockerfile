FROM ubuntu:20.04


RUN apt-get update -y && \
    apt-get install -y python3-pip python-dev
RUN pip3 install flask requests pandas

WORKDIR /app

COPY . /app

CMD flask run