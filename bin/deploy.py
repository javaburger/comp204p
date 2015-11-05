#!/usr/bin/env python

from fabric.api import *

local_ssh_port=1236;

env.user = 'localuser'
env.hosts = ['localhost:%d' % local_ssh_port]

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