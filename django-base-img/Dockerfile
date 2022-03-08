# Image used for django-based services
FROM python:3.10-slim
COPY /requirements.txt .
RUN apt update && \
    apt upgrade -y && \
    pip install --upgrade pip && \
    pip install -r requirements.txt
