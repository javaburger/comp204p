#!/bin/bash

NAME="ToDoListApp"
DJANGODIR=~/comp204p/app
BIND_ADDRESS=0.0.0.0:80
NUM_WORKERS=5
DJANGO_WSGI_MODULE=COMP204P.wsgi

echo "Starting $NAME as `whoami`"

cd $DJANGODIR

exec gunicorn ${DJANGO_WSGI_MODULE}:application --name $NAME --workers $NUM_WORKERS --bind=$BIND_ADDRESS
