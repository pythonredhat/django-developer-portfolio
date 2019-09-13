#pull base image
FROM python:3.7.4-alpine

#set working directory
WORKDIR /usr/src/app

#set enviornment variables
#don't let python write .pyc files
ENV PYTHONDONTWRITEBYTECODE 1
#ensure console output looks familiar, not buffered by docker
ENV PYTHONBUFFERED 1

#install psycopg2
RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add postgresql-dev \
    && pip install psycopg2 \
    && apk del build-deps

#install dependencies
RUN pip install --upgrade pip
RUN pip install pipenv
COPY ./Pipfile /usr/src/app/Pipfile
#need to explain below command, took out --dev as build fails with pylint
#pipenv system flag means install software onto os, not a virtualenv
#skip-lock means skip-lock file, it would be a dev install
RUN pipenv install --system --skip-lock

#copy project
COPY . /usr/src/app 

#run entrypoint.sh
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]

