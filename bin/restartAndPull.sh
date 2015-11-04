#!/bin/bash

cd /home/localuser;
git clone https://github.com/javaburger/comp204p.git || true;
cd /home/localuser/comp204p;
sudo systemctl stop gunicorn;
sudo pip install -r requirements.txt;
git reset --hard || true;
git pull origin master || true;
python manage.py syncdb;
sudo systemctl start gunicorn;