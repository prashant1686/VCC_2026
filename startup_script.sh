#! /bin/bash

apt-get update

# Installed web Server
apt-get install -y apache2 stress

#Installed Docker
apt-get install -y docker.io

# Start Services
systemctl start apache2
systemctl enable docker
systemctl start docker

# Created  a custom landing page
echo "<h1>Hybrid Lab Ready: $(hostname)</h1>" > /var/www/html/index.html
