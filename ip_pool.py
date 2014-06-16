#!/usr/bin/env python

import os,sys,struct,socket,time,multiprocessing

try:
    from netaddr import *
except:
    print 'please install python-netaddr first.'
    sys.exit()


if __name__ == '__main__':

    if len(sys.argv) <= 1:
        print "Usage:", os.path.basename(sys.argv[0]), "host"
        sys.exit()

    ip=IPNetwork(sys.argv[1])
    for x in list(ip):
        print x
