#!/usr/bin/env bash
<<<<<<< HEAD
# script that sets up web servers for the deployment of web_static
sudo apt-get update
sudo apt-get -y install nginx
sudo ufw allow 'Nginx HTTP'

sudo mkdir -p /data/
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
sudo touch /data/web_static/releases/test/index.html
sudo echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

sudo ln -s -f /data/web_static/releases/test/ /data/web_static/current

sudo chown -R ubuntu:ubuntu /data/

sudo sed -i '/listen 80 default_server/a location /hbnb_static { alias /data/web_static/current/;}' /etc/nginx/sites-enabled/default
=======
#sets up your web servers for the deployment of web_static.

sudo apt-get -y update
sudo apt-get -y install nginx

sudo mkdir -p /data/web_static/shared/  /data/web_static/releases/test/

sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

echo "Hello World" > /data/web_static/releases/test/index.html

sudo chown -R ubuntu /data/
sudo chgrp -R ubuntu /data/

new_config=\
"server {
        listen 80 default_server;
        listen [::]:80 default_server;
               root /var/www/html;
        index index.html index.htm index.nginx-debian.html;

        server_name _;
        add_header X-Served-By \$hostname;

	location /hbnb_static {
        alias /data/web_static/current;
        index index.html index.htm;
	}

        error_page 404 /404.html;
        location  /404.html {
            internal;
        }

        if (\$request_filename ~ redirect_me){
            rewrite ^ https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;
        }
}
"
echo "Ceci n'est pas une page" > /var/www/html/404.html
echo "$new_config" > /etc/nginx/sites-available/default

>>>>>>> cad2f8870189f452856cbf2ffe1f5e3ee3cb985d

sudo service nginx restart
