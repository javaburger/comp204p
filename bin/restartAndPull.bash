#!/bin/bash

cd /home/localuser;
git clone https://github.com/javaburger/comp204p.git || true;
cd /home/localuser/comp204p;
sudo systemctl stop gunicorn;
sudo pip install -r requirements.txt;
sudo git reset --hard || true;
sudo git pull origin master || true;
cd /home/localuser/comp204p/app;
python manage.py syncdb;
sudo systemctl start gunicorn;

echo `date "+%Y/%m/%d %H:%M:%S"`: Pulled changes from origin/master and restarted at as `whoami` >> /home/localuser/comp204p/logs.txt;