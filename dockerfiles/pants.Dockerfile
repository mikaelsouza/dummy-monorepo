FROM python:3.10-slim-bullseye

WORKDIR /pants/

RUN apt update

RUN apt install --no-install-recommends -y curl make git tar xz-utils

ADD scripts/get-pants.sh .

RUN chmod +x get-pants.sh

RUN ./get-pants.sh

ENV PATH=/root/bin:$PATH

RUN touch pants.toml

RUN PANTS_VERSION=2.17.0 pants -V

RUN rm pants.toml