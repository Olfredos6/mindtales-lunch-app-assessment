FROM python:3.10-slim
WORKDIR /auth-app
COPY ./src /auth-app
RUN apt update && \
    apt upgrade -y && \
    pip install --upgrade pip && \
    pip install -r requirements.txt
