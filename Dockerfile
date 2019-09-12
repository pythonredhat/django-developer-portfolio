#pull base image
FROM python:3.7-slim

#set enviornment variables
#don't let python write .pyc files
ENV PYTHONDONTWRITEBYTECODE 1
#ensure console output looks familiar, not buffered by docker
ENV PYTHONBUFFERED 1

#set working directory
WORKDIR /code

#install dependencies
RUN pip install pipenv
COPY Pipfile Pipfile.lock /code/
RUN pipenv install --system

#copy project
COPY . /code/

