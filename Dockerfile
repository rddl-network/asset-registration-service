FROM --platform=linux/amd64 python:3.10-slim AS base
FROM base AS builder

RUN apt-get update && apt-get -y upgrade
RUN apt-get install -y task-spooler
RUN pip install poetry

WORKDIR /usr/src/app
COPY ./main.py /usr/src/app/main.py
COPY ./poetry.lock /usr/src/app/poetry.lock
COPY ./pyproject.toml /usr/src/app/pyproject.toml
RUN mkdir /usr/src/app/templates
COPY ./templates/list_files.html /usr/src/app/templates/list_files.html

RUN poetry config virtualenvs.create false
RUN poetry install --no-root

EXPOSE 8000:8000

RUN adduser --system --group nonroot

RUN mkdir -p /var/www/html/.well-known
RUN chown nonroot:nonroot /var/www/html/.well-known

USER nonroot

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--timeout-keep-alive", "240", "--log-level=debug"]
