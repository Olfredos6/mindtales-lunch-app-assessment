FROM python:3.10-slim
WORKDIR restaurants-app
COPY ./src .
RUN apt update && \
    apt upgrade -y && \
    pip install --upgrade pip && \
    pip install -r requirements.txt