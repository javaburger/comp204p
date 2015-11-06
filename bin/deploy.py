#!/usr/bin/env python

from fabric.api import *

import os

env.user = 'localuser'
env.hosts = ['localhost:%s' % os.environ.get('LOCAL_SSH_PORT', 0)]

def deploy():
	run('git clone https://github.com/javaburger/comp204p.git || true')
	branch = os.environ.get("GITHUB_PULL_BRANCH")
	with cd('~/comp204p'):
		run('sudo systemctl stop gunicorn')
		run('sudo pip install -r requirements.txt')
		run('git reset --hard || true')
		run('git checkout ' + branch)
		run('git pull origin ' + branch + ' || true')
	with cd('~/comp204p/app'):
		run('python manage.py syncdb')
	with cd('~/comp204p/app'):
		run('sudo systemctl start gunicorn')