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

echo "Creating Flags"
mkdir /flags
echo "FoundTheGurl{IdentifyYourGurl}" > /flags/f1.txt
echo "FoundTheGurl{DumpsGuyCode}" > /flags/f2.txt
echo "FoundTheGurl{GotTheCulprit}" > /flags/f3.txt
echo "FoundTheGurl{SafeGuarded}" > /flags/f4.txt
chmod 777 /flags
chmod 777 /flags/f1.txt
chmod 777 /flags/f2.txt
chmod 777 /flags/f3.txt
chmod 777 /flags/f4.txt


echo "Runserver"
python3 manage.py runserver 0.0.0.0:8000

exec /bin/bash
