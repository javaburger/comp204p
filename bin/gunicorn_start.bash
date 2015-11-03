#!/bin/bash

NAME="ToDoListApp"
DJANGODIR=~/www/comp204p/COMP204P
BIND_ADDRESS=127.0.0.1:9000
NUM_WORKERS=5
DJANGO_WSGI_MODULE=COMP204P.wsgi

echo "Starting $NAME as `whoami`"

cd $DJANGODIR

exec gunicorn ${DJANGO_WSGI_MODULE}:application \
	--name $NAME \
	--workers $NUM_WORKERS \
	--bind=$BIND_ADDRESS