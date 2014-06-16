#!/bin/bash

# stop if errors occur
set -e

echo "Install python-netaddr, python-numpy package..."
sudo apt-get install python-netaddr python-numpy || \
    sudo yum install python-netaddr python-numpy

# clean ip.find.out
[ -f "ip.find.out" ] && rm -rf ip.find.out
touch ip.find.out

# we will scan all google's ip with 443 port
for i in $(ls gooole_ip_pool/* | sort -R)
do
    ./find_host_port.py $i | tee -a ip.find.out
done 

