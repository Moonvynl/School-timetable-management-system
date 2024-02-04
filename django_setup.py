import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoorm.settings')
django.setup()

from project.models import Subject

