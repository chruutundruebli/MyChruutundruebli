#!/bin/bash
nginx -g 'daemon off;' & 
./manage.py runserver 0.0.0.0:8000