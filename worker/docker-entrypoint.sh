#!bin/sh

server_ip=$1
echo -e "\nmaster-host=$server_ip" >> worker.conf
echo "server IP = $server_ip"
cat worker.conf
locust --config=worker.conf 