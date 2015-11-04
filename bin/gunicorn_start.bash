#!/bin/bash

NAME="ToDoListApp"
BIND_ADDRESS=0.0.0.0:80
NUM_WORKERS=5
DJANGO_WSGI_MODULE=COMP204P.wsgi

echo "Starting $NAME as `whoami`"

exec sudo gunicorn ${DJANGO_WSGI_MODULE}:application --pythonpath '/home/localuser/comp204p/app' --name $NAME --workers $NUM_WORKERS --bind=$BIND_ADDRESS