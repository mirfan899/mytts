#!/usr/bin/env bash

cp ./unicorn/gunicorn.socket /etc/systemd/system/
cp ./unicorn/gunicorn.service /etc/systemd/system/

sudo systemctl start gunicorn.socket
sudo systemctl enable gunicorn.socket
sudo systemctl status gunicorn.socket