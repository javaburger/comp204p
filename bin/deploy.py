#!/usr/bin/env python

from fabric.api import *

env.user = 'localuser'
env.hosts = ['localhost:1234']

def deploy():
	run('git clone https://github.com/javaburger/comp204p.git || true')
	with cd('~/comp204p'):
		run('sudo systemctl stop gunicorn')
		run('sudo pip install -r requirements.txt')
		run('sudo git reset --hard || true')
		run('sudo git pull origin master || true')
	with cd('~/comp204p/app'):
		run('python manage.py syncdb')
	with cd('~/comp204p/app'):
		run('sudo systemctl start gunicorn')