#pull base image
FROM python:3.7.4-alpine

#set working directory
WORKDIR /usr/src/app

#set enviornment variables
#don't let python write .pyc files
ENV PYTHONDONTWRITEBYTECODE 1
#ensure console output looks familiar, not buffered by docker
ENV PYTHONBUFFERED 1

#install dependencies
RUN pip install --upgrade pip
RUN pip install pipenv
COPY ./Pipfile /usr/src/app/Pipfile
#need to explain below command, took out --dev
RUN pipenv install --system --skip-lock

#copy project
COPY . /usr/src/app 

