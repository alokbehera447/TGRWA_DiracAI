#Programming protocols: 
  -  Safe from bugs
  -  Easy to understand
  -  Ready for change

#  1.Instructions to setup the server
  1-4 could be found here: [DigitalOcean](https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-20-04)


 -  `ssh root@your_server_ip` #login to root user

 -  `adduser sammy` # add a user

 -  `usermod -aG sudo sammy`  # add previleges
 
    #Ubuntu 20.04 servers can use the UFW firewall to make sure only connections to certain services are allowed

 -  `ufw app list`

 -  `ufw allow OpenSSH` # We need to make sure that the firewall allows SSH connections so that we can log back in next time

 -  `ufw enable` # enable firewall
 -  `ufw status` 
   
     ![alt text](https://github.com/bmahakud/edResearch/blob/main/ufwstatus.png "Logo Title Text 1")  
     
     #Above command will tell if the firewall is active or dead. Also which connections are allowed.
     As the firewall is currently blocking all connections except for SSH, if you install and configure additional services, you will need to adjust the firewall      settings to allow traffic in. Upon installation, applications that rely on network communications will typically set up a UFW profile that you can use to    allow connection from external addresses. More info could be found here [more ufw info](https://www.digitalocean.com/community/tutorials/ufw-essentials-common-firewall-rules-and-commands)
     
 -  `sudo ufw deny from 203.0.113.100` # use this command in case you want to block any ip.
  
 
 #  2.Set Up Django with Postgres, Nginx, and Gunicorn
 
 -  `sudo apt update`
 -  `sudo apt install python3-pip python3-dev libpq-dev postgresql postgresql-contrib nginx curl`
 -  `sudo -u postgres psql`
 -  `postgres=#  CREATE DATABASE myproject;`
 -  `postgres=#  postgres=#  CREATE USER myprojectuser WITH PASSWORD 'password';`
 -  `postgres=#  ALTER ROLE myprojectuser SET client_encoding TO 'utf8';`
 -  `postgres=#  ALTER ROLE myprojectuser SET default_transaction_isolation TO 'read committed';`
 -  `postgres=#  ALTER ROLE myprojectuser SET timezone TO 'UTC';`
 -  `postgres=#  GRANT ALL PRIVILEGES ON DATABASE myproject TO myprojectuser;`
 -  `postgres=# \l`  #list all databases
 -  `postgres=# \c myproject;` #change to newly created database
 -  `myproject=# ` # now you are in myproject database
 -  `myproject=# \dt` #list tables
 -  `myproject=# \q` # exit
 -  `sudo -H pip3 install --upgrade pip`
 -  `sudo -H pip3 install virtualenv`
 -  `mkdir ~/myprojectdir`
 -  `cd ~/myprojectdir`
 -  `virtualenv myprojectenv`
 -  `source myprojectenv/bin/activate`
 -  `pip install django gunicorn psycopg2-binary`
 -  `django-admin startproject myproject`
 -  #edit settings.py file properly 


 #change the following in the settings.py to connect to postgres database
 -  `
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'myproject',
        'USER': 'myprojectuser',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '',
    }
}`

-  `sudo ufw allow 8000`
-  `python3 manage.py runserver 0.0.0.0:8000`
-  Now you should see the django installation page in your ip or domain

#website can be viewed here http://server_domain_or_IP:8000


#TEST  gunicorn's ability to serve the project
-  `cd ~/myprojectdir`
-  `gunicorn --bind 0.0.0.0:8000 myproject.wsgi`
-  This will start Gunicorn on the same interface that the Django development server was running on. You can go back and test the app again.

# 3.Creating systemd Socket and Service Files for Gunicorn

-  `sudo vi /etc/systemd/system/gunicorn.socket`
  #fill [this](https://github.com/bmahakud/edResearch/blob/main/gunicorn.socket) content in gunicorn.socket


-  `sudo vi /etc/systemd/system/gunicorn.service` # open this file and fill [this info](https://github.com/bmahakud/edResearch/blob/main/gunicorn.service)




-  `sudo systemctl start gunicorn.socket`
-  `sudo systemctl enable gunicorn.socket`
-  `sudo systemctl status gunicorn.socket`# test socket activation
-  `sudo systemctl daemon-reload`
-  `sudo systemctl restart gunicorn`

# 4.Configure  Nginx to Proxy Pass to Gunicorn

-  `sudo vi /etc/nginx/sites-available/myproject` and put [this](https://github.com/bmahakud/edResearch/blob/main/myproject) content in this file
-  `sudo ln -s /etc/nginx/sites-available/myproject /etc/nginx/sites-enabled`
-  `sudo nginx -t` # test for syntax errors
-  `sudo systemctl restart nginx`
-  `sudo ufw delete allow 8000`
-  `sudo ufw allow 'Nginx Full'`


# 5.Let's encrypt SSL
-  [DigitalOceanLink](https://www.digitalocean.com/community/tutorials/how-to-secure-nginx-with-let-s-encrypt-on-ubuntu-20-04)
-  `sudo systemctl status certbot.timer`  check the status of SSL certificate
-  Location of keys: /etc/letsencrypt/live/edresearch.co.in
 

#  6.Deploying Django Channels with Daphne & Systemd ref. [codewithmitch](https://github.com/mitchtabian/HOWTO-django-channels-daphne)
-  `python -m pip install -U channels`
-  `pip install redis`
-  `python3 -m pip install channels_redis`
-  `sudo apt install daphne`
-  `sudo vi /etc/systemd/system/daphne.service`  # fill [this](https://github.com/bmahakud/edResearch/blob/main/daphne.service) content 
-  `sudo systemctl daemon-reload`

-  `sudo systemctl start daphne.service`

-  `sudo systemctl status daphne.service`
-  Open a file `boot.sh` inside `/root` folder and put this line `sudo systemctl start daphne.service`
-  `sudo vi /etc/systemd/system/on_boot.service`  and put [this](https://github.com/bmahakud/edResearch/blob/main/on_boot.service) 
-  `systemctl daemon-reload`
-  `sudo systemctl start on_boot`
-  `sudo systemctl enable on_boot`
-  `ufw allow 8001`
-  `systemctl status on_boot.service`
-  `systemctl status daphne.service`
-  `sudo shutdown -r now`


# 7. Docker instructions and commands

  -  Installation instructions: [dockerdocsLink](https://docs.docker.com/engine/install/ubuntu/) # follow from repository
  -  Install-command-1:  `sudo apt-get update`
  -  Install-command-2:
   
     ```sudo apt-get install \  
      apt-transport-https \  
      ca-certificates \  
      curl \  
      gnupg \  
      lsb-release 
     ```    
  -  Install-command-3: `curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg` # Add docker's official GPG key
  -  Install-command-4: 
  
     ```echo \    
       "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \    
       $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null    
     ```
     
  -  Install-command-5: `sudo apt-get update`
  -  Install-command-6:  `sudo apt-get install docker-ce docker-ce-cli containerd.io`
  
  
  
    # initial setup commands 
   -  [dcoker permission denied issue](https://stackoverflow.com/questions/48957195/how-to-fix-docker-got-permission-denied-issue)
   
   -  1.  `sudo groupadd docker` #  Create the docker group if it does not exist
   -  2.  `sudo usermod -aG docker $USER` #Add your user to the docker group.
   -  3.  `newgrp docker`   #Run this command or Logout and login again and run 
   
   
   
    
    # operation commands
  -  `ps aux` # view which processes are running on which port  
  -  `sudo docker pull postgres` # pulls the postgres image
  -  `sudo docker start contanerid # starts the container, not the image
  -  `sudo docker stop contanerid # stops the container, not the image
  -  `sudo docker run postgres:13.4` #pull the image postgress 13.4 and starts it
  -  `sudo docker ps ` # shows which containers are  running
  -  `sudo docker ps -a` # shows all containers running and not running
  -  `sudo docker images` # will show existing images
  -  `sudo docker run -d redis` #run in detached mode
  -   two containers can run on one port as long as they bind to different ports on he host machine
  -   `sudo docker run -p 6379:6379 -d redis:5` # first port no is the host machine port and the second one is the port on which docker is listening
  -   `sudo docker logs containerid` # gives details about why application is not connecting to etc.
  -   `sudo docker run -p 6379:6379 -d --name redisnew redis:5` # creates new container with name redisnew
  -   `sudo docker exec -it containerid /bin/bash` # go to docker terminal and debug 
  -   `root@34b9faa14455:/data# `
  -   `root@34b9faa14455:/data# cd`
  -   `root@34b9faa14455:~# cd ../ `
  -   `root@34b9faa14455:~# env` # prints the environment variables for checking correct setting
  -   #demo project commands
  -   `sudo docker network create mongo-network` creates network to hold different containers connected
  -   `sudo docker network ls` # list available networks
  -   `sudo docker run -p 27017:27017 -d -e MONGO_INITDB_ROOT_USERNAME=admin -e MONGO_INITDB_ROOT_PASSWORD=password --name mongodb --net mongo-network mongo` #run mngodb within the mongo-network
  -   `sudo docker run -d  -p8081:8081 -e ME_CONFIG_MONGODB_ADMINUSERNAME=admin -e ME_CONFIG_MONGODB_ADMINPASSWORD=password --name mongo-express --net mongo-network -e ME_CONFIG_MONGODB_SERVER=mongodb mongo-express` # run mongo express and connect to mongo DB wihin mongo-network


# 7. Useful Links

  -  [Django Channel Examples: Andrew Godwin](https://github.com/andrewgodwin/channels-examples)
  -  [YotubeLink: Django Channels, Websockets, Ngnix, Gunicorn, Daphne-->Production](https://www.youtube.com/watch?v=EdK15Qcc3Zs)
  -  [Transparent Bkg Images](https://www.pngall.com/)
  -  [LMSs in INDIA](https://www.softwaresuggest.com/learning-management-system)
  -  [Install Java](https://www.youtube.com/watch?v=ogWKP9Lm-Qo) 
  -  [Install Android Studio](https://www.youtube.com/watch?v=x3nVHXv3oyw)
  -  [Deploy To AWS ](https://github.com/PaulleDemon/AWS-deployment#deploying-a-web-application-to-aws-django-django-channels)
  - [Generate Access Token Twilio](https://www.twilio.com/blog/generate-access-token-twilio-chat-video-voice-using-twilio-functions#:~:text=Visit%20the%20API%20Key%20section,that%20says%20Create%20API%20Key.)
  - [Install Nginx, MySQL, PHP](https://www.digitalocean.com/community/tutorials/how-to-install-linux-nginx-mysql-php-lemp-stack-on-ubuntu-20-04)
  - [Uninstall MySQL](https://www.digitalocean.com/community/questions/completely-uninstall-mysql-server)
  - [WordPress Installation](https://www.digitalocean.com/community/tutorials/how-to-install-wordpress-with-lemp-on-ubuntu-20-04) 
  - [Andrew Godwin about scaling Django](https://groups.google.com/g/django-developers/c/zfkk_nX3C5c)
  - [About Websockets youtube talk](https://www.youtube.com/watch?v=8ARodQ4Wlf4)
  - [Scaling Django with PostgreSQL replicas](https://andrewbrookins.com/python/scaling-django-with-postgres-read-replicas/)
  - [From Django Cons 2022: Django Experts](Carlton Gibson)
  - [Learn Django from founder Will Vincent](https://learndjango.com/)
  - [Django Deployement Checklist](https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/)
  - [Django Scale: Carl Meyer](https://www.youtube.com/watch?v=lx5WQjXLlq8)
  - [Scaling Django with MySQL](https://www.youtube.com/watch?v=bq9BThgF6jc)
# CelpipSoftware
