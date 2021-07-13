FROM python:3.8-alpine
MAINTAINER Mortaza Samadpoor

#Setting PYTHONUNBUFFERED to a non empty value ensures that the python output is sent straight to terminal (e.g. your container log) without being first buffered and that you can see the output of your application (e.g. django logs) in real time.
#This also ensures that no partial output is held in a buffer somewhere and never written in case the python application crashes.
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN apk add --update --no-cache postgresql-client
RUN apk add --update --no-cache --virtual .tmp-build-deps \
    gcc libc-dev linux-headers postgresql-dev
RUN pip install -r /requirements.txt
RUN apk del .tmp-build-deps

#create empty folder(/app) on our docker image
RUN mkdir /app
#as default directory
WORKDIR /app
#copy from our local machine to our docker image
COPY ./app /app


#security purposes
#if you don't create user then the image will run our application using the root account which is not recommended
# if you create a separate user just for our application then this kind of limits the scope that an attacker would have in our documentation.
#create a user that is going to run our application using docker only
RUN adduser -D user
#switch docker to the user
USER user

#terminal: docker build .  -> create image file
