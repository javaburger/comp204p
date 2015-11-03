#!/usr/bin/env python

from fabric.api import *

env.user = 'localuser'
env.hosts = ['localhost:1234']

def deploy():
	run('git clone https://github.com/javaburger/comp204p.git')
	cd('~/comp204p')
	run('git pull origin master')
	cd('~/comp204p/app')
	run('python manage.py syncdb')
	cd('~/comp204p/bin')
	run('sudo ./gunicorn_start.bash')