#!/usr/bin/env python

from fabric.api import *

env.user = 'localuser'
env.hosts = ['localhost']

def deploy():
	run('git clone https://github.com/javaburger/comp204p.git')
	run('')