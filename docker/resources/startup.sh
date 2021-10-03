#!/bin/bash

./manage.py migrate
./manage.py collectstatic --noinput

if [ -e first_startup.txt ]; then
  ./manage.py createsuperuser --noinput --username superadmin --email superadmin@localhost
  ./manage.py create_member_for_superusers
  ./manage.py generate_testdata_advanced
  rm -rf first_startup.txt
fi

nginx -g 'daemon off;' & 
./manage.py runserver 0.0.0.0:8000