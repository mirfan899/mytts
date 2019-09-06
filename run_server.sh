#!/usr/bin/env bash

source .mytts/bin/activate
nohup python manage.py runserver 0.0.0.0:8000 >> output.log 2>&1 &