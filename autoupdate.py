import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
django.setup()

from project.sheets import *
from project.helpers import *

update_call_data()
extract_and_download_records()

