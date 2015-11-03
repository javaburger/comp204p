#!/usr/bin/env python

from fabric.api import *

env.user = 'localuser'
env.hosts = ['localhost:1234']

def deploy():
	# run('git clone https://github.com/javaburger/comp204p.git')
	with cd('~/comp204p'):
		run('sudo killall gunicorn')
		run('git reset --hard')
		# run('git clean -f -d')
		# run('git clean -f -x -d')
	with cd('~/comp204p/app'):
		run('python manage.py syncdb')
	with cd('~/comp204p/bin'):
		run('sudo ./gunicorn_start.bash')