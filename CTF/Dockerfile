# Use the official Ubuntu base image
FROM ubuntu:20.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y curl wget unzip python3 python3-pip nano

RUN pip3 install requests virtualenv

COPY FUG /var/www/html/
COPY requirements.txt /var/www/html/

RUN adduser --disabled-password --gecos "" foundyourgurl && \
    echo "foundyourgurl:PassCodeXUV" | chpasswd && \
    usermod -aG sudo foundyourgurl


COPY ./script.sh /var/www/html/
RUN chmod 777 /var/www/html/script.sh

WORKDIR /var/www/html/
RUN rm db.sqlite3

RUN python3 -m virtualenv venv


CMD [ "/bin/sh"]
ENTRYPOINT ["/var/www/html/script.sh"]
