#!/bin/sh

#halt on any error
set -e

#all env variables inherited from docker-compose
#wait for database to come up
if [ "$DATABASE" = "postgres" ]
then
  echo "Waiting for postgres..."
  while ! timeout 5 bash -c 'cat < /dev/null > /dev/tcp/$SQL_HOST/$SQL_PORT'; do
    sleep 0.1
  done
  #while ! echo > /dev/tcp/$SQL_HOST/$SQL_PORT && echo "Port is open"; do
  #while ! nmap $SQL_HOST -p $SQL_PORT; do
  #while ! nc -z $SQL_HOST $SQL_PORT; do
  #  sleep 0.1
  #done

  echo "PostgreSQL started"
fi

#reset database
python ./django_developer_portfolio/manage.py flush --no-input
#migrate database
python ./django_developer_portfolio/manage.py migrate
#serve static files
python ./django_developer_portfolio/manage.py collectstatic --no-input --clear
#load fake data via fixtures
python ./django_developer_portfolio/manage.py loaddata ./django_developer_portfolio/projects/fixtures/projects.json
#load fake data via management commands
python ./django_developer_portfolio/manage.py add_fake_blog_posts
python ./django_developer_portfolio/manage.py add_fake_versions

#It does nothing except pass control back to whatever process is ran in your CMD instruction in your Dockerfile. That’s what exec "$@" does.
exec "$@"