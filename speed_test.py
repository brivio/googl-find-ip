#!/usr/bin/env python

import os,sys,struct,socket,time,multiprocessing

ip=[]
time_swap=[]

def ping_test(host):
    cmd='ping -c5 '+host
    out=os.popen(cmd).read()
    out=[x for x in out.split('\n') if x]
    try:
        print host, out[-1], out[-2]
    except:
        pass

def chunks(l, n):
    """ Yield successive n-sized chunks from l.
    """
    for i in xrange(0, len(l), n):
        yield l[i:i+n]

if __name__ == '__main__':

    if len(sys.argv) <= 1:
        print "Usage:", os.path.basename(sys.argv[0]), "host1|host2"
        sys.exit()
    else:
        filename=sys.argv[1]
        with open(filename, 'r') as infile:
            ip=infile.readlines()

        ip=ip[0].rstrip('\n')
        ip=ip.split('|')
        ip=[x for x in ip if x]
        ip=list(chunks(ip,10))

        for x in ip:
            for i in x:
                dmn_dtct = multiprocessing.Process(name='ping_test',
                                                   target=ping_test,
                                                   args=(i,))
                dmn_dtct.daemon=True
                dmn_dtct.start()
    
            dmn_dtct.join()
