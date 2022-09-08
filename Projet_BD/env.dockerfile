FROM python3.8.10-slim-buster
RUN apt-get install pip3 \
    apt-get install vim

COPY requirement.txt requirement.txt

RUN pip3 install -r requirement.txt

CMD