#!/bin/bash
cd /app
./manage.py collectstatic --no-input
./manage.py migrate --no-input
uwsgi --ini uwsgi.ini
