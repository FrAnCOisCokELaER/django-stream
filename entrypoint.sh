#!/bin/sh
echo "Django DB clean up"
cd ../template && rm -f ./data/db.sqlite3 2> /dev/null   
echo "Django migration"
python3 manage.py migrate &&
python3 manage.py collectstatic &&
nbworkers=$((2*$(grep -c ^processor /proc/cpuinfo)+1)) 
echo "Starting Django Gunicorn server on port 8010 with ${nbworkers} workers ..."
gunicorn --workers=${nbworkers} -b 0.0.0.0:8010 template.wsgi &
#DEBUG MODE# python3 ../manage.py runserver 0.0.0.0:${SIDE_CAR_PORT} &