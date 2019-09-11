### Requirment
Python 3.7.*

### mytts 
Django app for Cantonese synthesizer

### Compile Ossian
Run this in Ossian directory
```shell script
./scripts/setup_tools.sh mirfan899 Tqveb=Be
```

### IP of Allowed Hosts.
After cloning the repository add IP address in settings in allowed hosts.

### Install NGINX
```shell script
sudo apt-get install nginx
```
### Gunicorn
copy `gunicorn.socket` to `/etc/systemd/system/`
```shell script
cp ./unicorn/gunicorn.socket /etc/systemd/system/
cp ./unicorn/gunicorn.service /etc/systemd/system/
```

Now enable the service
```shell script
sudo systemctl start gunicorn.socket
sudo systemctl enable gunicorn.socket
sudo systemctl status gunicorn.socket
```

### NGINX configuration
copy mytts to `/etc/nginx/sites-available/`
test it 
enable site
```shell script
sudo ln -s /etc/nginx/sites-available/mytts /etc/nginx/sites-enabled
```

Other NGINX, GUNICORN commands
```shell script
sudo nginx -t
sudo systemctl restart nginx
sudo systemctl restart gunicorn
sudo systemctl restart gunicorn.socket gunicorn.service
```
### Free Django port
```shell script
sudo lsof -t -i tcp:8000 | xargs kill -9
```

### AppEngine
`main.py` is for AppEngine