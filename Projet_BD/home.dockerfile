FROM ubuntu
RUN apt-get update \
    apt-get  install python3 \
    apt-get  install pip \
    apt-get  install vim \
    apt-get  install virtualenv \
    apt-get  install jupyter

RUN pip install -r requirement.txt