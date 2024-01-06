FROM python:3.10-bookworm

WORKDIR /pants/

RUN apt update

RUN apt install --no-install-recommends -y curl make git tar xz-utils gcc python3-dev

ADD scripts/get-pants.sh .

RUN chmod +x get-pants.sh

RUN ./get-pants.sh

ENV PATH=/root/bin:$PATH
