#!/usr/bin/env bash

# Use this script to deploy start the app
# create necessary folder if they do not exist already
# data folder for the postgres service
if [ ! -d ./services/postgres/data ]; then
  mkdir -p ./services/postgres/data;
fi


# build the base image for django apps
( cd django-base-img && docker build -t base-django:latest . && cd .. )

# build all the services
docker-compose build

# # compose start services
docker-compose up -d

# wait for postgres to come up before starting to apply migrations
./wait-for-it.sh 127.0.0.1:5432 -t 5 -- echo "Starting deployment..."

echo ============ auth ====================
docker-compose exec auth  bash -c 'python manage.py makemigrations && python manage.py migrate core'
docker-compose exec auth python manage.py migrate
echo ============ restaurants ====================
docker-compose exec restaurants bash -c 'python manage.py makemigrations &&  python manage.py migrate'
echo ============ votes ====================
docker-compose exec votes bash -c 'python manage.py makemigrations && python manage.py migrate'

docker-compose logs -f