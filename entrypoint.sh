#!/bin/sh

#halt on any error
set -e

#all env variables inherited from docker-compose
#wait for database to come up
if [ "$DATABASE" = "postgres" ]
then 
  echo "Waiting for postgres..."
  while ! curl $SQL_HOST:$SQL_PORT
  #while ! nc -z $SQL_HOST $SQL_PORT; do
    sleep 0.1
  done

  echo "PostgreSQL started"
fi

#reset database
python ./django_developer_portfolio/manage.py flush --no-input
#migrate database
python ./django_developer_portfolio/manage.py migrate

#It does nothing except pass control back to whatever process is ran in your CMD instruction in your Dockerfile. That’s what exec "$@" does.
exec "$@"