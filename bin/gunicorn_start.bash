#!/bin/bash

NAME="ToDoListApp"
BIND_ADDRESS=unix:/home/localuser/comp204p/app.sock
NUM_WORKERS=5
DJANGO_WSGI_MODULE=COMP204P.wsgi

echo "Starting $NAME as `whoami`"

exec gunicorn ${DJANGO_WSGI_MODULE}:application --pythonpath '/home/localuser/comp204p/app' --name $NAME --workers $NUM_WORKERS --bind=$BIND_ADDRESS