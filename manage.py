#!/usr/bin/env python
import os
import sys

activate_this = 'env/bin/activate_this.py'
if os.path.exists(activate_this):
    execfile(activate_this, dict(__file__=activate_this))

if __name__ == "__main__":
    if os.geteuid() == 0:
        exit("You can't run script as superuser")

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tttt.settings.production")

    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
