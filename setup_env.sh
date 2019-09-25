#!/bin/bash


#public
echo DEBUG=1 >> .env 
echo SQL_ENGINE=django.db.backends.postgresql >> .env 
echo SQL_DATABASE=postgres >> .env  
echo ENABLE_PIPENV=true >> .env  

#gitlab secret
echo SECRET_KEY=$SECRET_KEY >> .env
echo SQL_DATABASE=$SQL_DATABASE >> .env
echo SQL_USER=$SQL_USER >> .env
echo SQL_PASSWORD=$SQL_PASSWORD >> .env 
echo SQL_HOST=$SQL_HOST >> .env
echo SQL_PORT=$SQL_PORT >> .env 
