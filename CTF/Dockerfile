# Use the official Ubuntu base image
FROM ubuntu:20.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y curl wget unzip python3 python3-pip nano

RUN pip3 install requests virtualenv

COPY FUG /var/www/html/
COPY requirements.txt /var/www/html/

RUN echo "got_the_evidence{Evidence_found_bhaiya}" > flag.txt
RUN echo "Setting password for: root"
RUN echo "root:12345678" | chpasswd
RUN echo "Password changed"

COPY ./script.sh /var/www/html/
RUN chmod 777 /var/www/html/script.sh

WORKDIR /var/www/html/
RUN rm db.sqlite3

RUN python3 -m virtualenv venv

EXPOSE 8000

CMD [ "/bin/sh"]
ENTRYPOINT ["/var/www/html/script.sh"]
