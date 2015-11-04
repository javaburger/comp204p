#!/bin/bash
echo starting pull and restart at `date "+%Y/%m/%d %H:%M:%S"`\\n >> /home/localuser/comp204p/logs.txt;
cd /home/localuser;
echo cloning at `date "+%Y/%m/%d %H:%M:%S"`\\n >> /home/localuser/comp204p/logs.txt;
git clone https://github.com/javaburger/comp204p.git || true;
cd /home/localuser/comp204p;
echo stopping gunicorn `date "+%Y/%m/%d %H:%M:%S"`\\n >> /home/localuser/comp204p/logs.txt;
sudo systemctl stop gunicorn;
sudo pip install -r requirements.txt;
git reset --hard || true;
echo pulling changes `date "+%Y/%m/%d %H:%M:%S"`\\n >> /home/localuser/comp204p/logs.txt;
git pull origin master || true;
cd /home/localuser/comp204p/app;
python manage.py syncdb;
sudo systemctl start gunicorn;
echo restarted at `date "+%Y/%m/%d %H:%M:%S"`\\n >> /home/localuser/comp204p/logs.txt;