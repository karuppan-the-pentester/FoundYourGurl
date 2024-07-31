#!/usr/bin/bash

echo "Changing Directory"
cd /var/www/html/

echo "Venv"
source venv/bin/activate
pip install Django pillow tzdata

echo "Migrating"
python3 manage.py makemigrations
python3 manage.py migrate
python3 DBMaker.py

echo "Runserver"
python3 manage.py runserver 0.0.0.0:8000

exec /bin/bash
