#!/usr/bin/env bash

# Use this script to deploy start the app

# create necessary folder if they do not exist already
# data folder for the postgres service
if [ ! -d ./services/postgres/data ]; then
  mkdir -p ./services/postgres/data;
fi


# start all the services
docker-compose up