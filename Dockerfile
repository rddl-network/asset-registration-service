FROM --platform=linux/amd64 python:3.10-slim AS base
FROM base AS builder

RUN apt-get update && apt-get -y upgrade
RUN pip install poetry

WORKDIR /usr/src/app
COPY . /usr/src/app

RUN poetry config virtualenvs.create false
RUN poetry install --no-root

EXPOSE 8000:8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--timeout-keep-alive", "240", "--log-level=debug"]
