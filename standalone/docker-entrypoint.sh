#!bin/sh

host_ip=$1
echo -e "\nhost = http://$host_ip:8069" >> standalone.conf
cat standalone.conf
locust --config=standalone.conf 