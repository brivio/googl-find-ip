#!/bin/bash

[ ! -f "ip.find.out" ] && echo "Please run find_ip.sh first" && exit

# format ip
cat ip.find.out | xargs | sed 's/ /|/g' | tee ip.format

# test ping
echo "test ping, please wait..."
./speed_test.py "ip.format" | tee ping.out

# sort ip
./speed_sort.py

echo "Please update your proxy.ini, and restart goagent"
echo "Wait for several minutes to use goagent"

