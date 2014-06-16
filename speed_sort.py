#!/usr/bin/env python

import os,sys

try:
    import numpy as np
except:
    print 'please install python-numpy first'
    print 'sudo apt-get install python-numpy'
    sys.exit()

with open('ping.out', 'r') as ping_f:
    ping_out = ping_f.read()

text_list=[x for x in ping_out.split('\n')]
text_list=[x for x in text_list if not "100%" in x]
text_list=[x for x in text_list if x]

if len(text_list)==0:
    print 'Oops, can NOT ping any ip in ip.find.out, please check your network'
    sys.exit()

text_list=[x.split() for x in text_list]

# get all ips
ip_list=[x[0] for x in text_list]
speed_list=[x[4] for x in text_list]
speed_list=[x.split('/') for x in speed_list]
speed_list=[x[1] for x in speed_list]

# convert to numpy array
ip_np=np.array(map(float, range(0,len(ip_list))))
speed_np=np.array(map(float, speed_list))

# sort
ip_speed_np=np.array([ip_np, speed_np])
ip_speed_np=ip_speed_np.T
ip_address_order=np.lexsort((ip_speed_np[:,0],ip_speed_np[:,1]))

ip_out=''
for i in ip_address_order:
    ip_out+=ip_list[i]+'|'

# write to 'ip.final' file
ip_out_f=open('ip.final', 'w')
ip_out_f.write(ip_out[:-1])
ip_out_f.close()

print
print 'valid ip is: '
print ip_out[:-1]
print
print
