#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then 
  echo "Waiting for postgres..."

  while ! nc -z $SQL_HOST $SQL_PORT; do
    sleep 0.1
  done

  echo "PostgreSQL started"
fi

python ./django_developer_portfolio/manage.py flush --no-input
python ./django_developer_portfolio/manage.py migrate
exec "$@"