from ubuntu:14.04
MAINTAINER max@meldrum.se

RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential

COPY . /enya
WORKDIR /enya
RUN pip install nameko
# Base CMD. It is overwritten when i send in the custom nameko command with the right ip address.
CMD ["nameko", "run", "logger", "--broker", "amqp://guest:guest@localhost"]

