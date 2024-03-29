FROM python:3.11.7-slim-bullseye

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DEBUG 1

RUN pip install --upgrade pip

COPY ./projeto/requirements.txt .

RUN pip install -r requirements.txt

COPY ./projeto /app

WORKDIR /app

COPY ./entrypoint.sh /
ENTRYPOINT [ "sh", "/entrypoint.sh" ]
