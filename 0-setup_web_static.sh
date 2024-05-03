#!/usr/bin/env bash
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


sudo service nginx restart
