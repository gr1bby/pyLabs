FROM python:3.10

ARG WORKDIR=/code

WORKDIR ${WORKDIR}

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY src/ src
COPY test/ test
COPY .env .

ENV PYTHONPATH=${WORKDIR}/src

ENTRYPOINT [ "python" ]
