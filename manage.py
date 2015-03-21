#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    if 'test' in sys.argv[1:2]:
        # While testing we need to make sure we don't use any local overrides.
        default = 'signing_service.settings.test'
    else:
        default = 'signing_service.settings'
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', default)

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
