#!/bin/bash

rm -rf docker/resources/MyChruutundruebli
mkdir docker/resources/MyChruutundruebli

cp -r __pycache__ docker/resources/MyChruutundruebli
cp -r chruutundruebli docker/resources/MyChruutundruebli
cp -r dbexport docker/resources/MyChruutundruebli
cp -r templates docker/resources/MyChruutundruebli
cp manage.py docker/resources/MyChruutundruebli
cp README.md docker/resources/MyChruutundruebli
cp requirements.txt docker/resources/MyChruutundruebli

docker-compose -f docker/docker-compose.yml build