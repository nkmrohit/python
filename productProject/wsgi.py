"""
WSGI config for productProject project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os
import sys
from django.conf import settings
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'productProject.settings')
sys.path.append(os.path.join(settings.BASE_DIR, "customers"))
sys.path.append(os.path.join(settings.BASE_DIR, "vendors"))
sys.path.append(os.path.join(settings.BASE_DIR, "superadmin"))

application = get_wsgi_application()
