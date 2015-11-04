"""
WSGI config for COMP204P project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import sys, os

from django.core.wsgi import get_wsgi_application

sys.path.insert(0, '/home/localuser/comp204p/app')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "COMP204P.settings")
application = get_wsgi_application()