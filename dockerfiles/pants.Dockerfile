FROM python:3.10-slim-bookworm

WORKDIR /pants/

RUN apt update

RUN apt install --no-install-recommends -y curl make git tar xz-utils gcc

ADD scripts/get-pants.sh .

RUN chmod +x get-pants.sh

RUN ./get-pants.sh

ENV PATH=/root/bin:$PATH

ADD pants.toml pants.toml

RUN pants -V

RUN rm pants.toml