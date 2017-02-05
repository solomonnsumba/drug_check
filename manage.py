#!/usr/bin/env python
#python manage.py runserver 192.168.43.156:8000

import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pharmacy_serve.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
