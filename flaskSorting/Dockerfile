FROM python:3.10

ARG WORKDIR=/code

WORKDIR ${WORKDIR}

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY alembic/ alembic
COPY alembic.ini .

COPY src/ src
COPY tests/ tests
COPY .env .

ENV PYTHONPATH=${WORKDIR}/src

ENTRYPOINT [ "python" ]
