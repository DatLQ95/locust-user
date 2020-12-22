#!bin/sh

host_ip=$1
echo -e "\nhost = http://$host_ip:8069" >> master.conf
cat master.conf
locust --config=master.conf