#!/bin/bash

cd /home/localuser;
git clone https://github.com/javaburger/comp204p.git || true;
cd /home/localuser/comp204p;
sudo systemctl stop gunicorn;
sudo pip install -r requirements.txt;
git reset --hard || true;
git pull origin master || true;
cd /home/localuser/comp204p/app;
python manage.py syncdb;
sudo systemctl start gunicorn;
echo restarted at `date "+%Y/%m/%d %H:%M:%S"`\\n >> /home/localuser/comp204p/logs.txt