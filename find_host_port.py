#!/usr/bin/env python

import os,sys,struct,socket,time,multiprocessing
from itertools import islice
import httplib


thread_num=100

try:
    from netaddr import *
except:
    print 'please install python-netaddr first.'
    sys.exit()

def port_detect(hostname):

    try:
        c = httplib.HTTPSConnection(hostname, timeout=3)
        c.request("GET", "/")
        response = c.getresponse()
        result=str(response.status)+' '+response.reason
        if '200 OK' in result:
            print hostname
    except:
        pass

if __name__ == '__main__':

    if len(sys.argv) <= 1:
        print "Usage:", os.path.basename(sys.argv[0]), "host"
        sys.exit()

    filename=sys.argv[1]

    with open(filename, 'r') as infile:
        lines=infile.readlines(10)
        while lines:
            lines=[x.rstrip('\n') for x in lines]

            for ip in lines:
                dmn_dtct = multiprocessing.Process(name='port_detect',
                                                   target=port_detect,
                                                   args=(ip,))
                dmn_dtct.daemon=True
                dmn_dtct.start()
    
            dmn_dtct.join()

            lines=infile.readlines(thread_num)
