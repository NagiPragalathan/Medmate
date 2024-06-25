import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Medmate.settings")

application = get_wsgi_application()

# For Vercel
app = application
