#!/usr/bin/env python

import socket,time
# from collections import OrderedDict # needed for options to be in order!
from libs.fuzzers import *
from collections import OrderedDict
# you can import directly from higher dir?
from libs.helpers import *

""" this fuzzer module is meant to work with WuFu only """

# we need to set a base standard for making modules... 
class ModuleFuzzer():
    # no need for global.. use __init__ and self :]
    def __init__(self):
        # self.opts = OrderedDict({ 
        #  not sure why OrdDict isnt working.. leaving for now as it doesnt afffect much
        self.opts = OrderedDict({
                    # all opts must be lower fyi...
                    'target'  : ['127.0.0.1',           True,  'Target IP Address'],
                    'port'    : ['21',                  True,  'Port on which service is running'],
                    'buffer'    : [10,                  True,  'Integer to be doubled'],
                })
        dis = """Simple FTP Fuzzer, doubles defined integer by 1 and sends over defined target
                      NOTE : The main crshing buffer value will probably be one less double"""
        self.info = {
                    'Name'             : 'Loop FTP Fuzzer',
                    'Description'      : dis,
                    'Author'           : '@bofheaded'
                }

    def executer(self, option):
        buf = option["buffer"]
        tar = option['target']
        port = option['port']
        mul_buf=buf
        print ("[!] Executing fuzzer on %s:%s" % (tar, port))
        sock = socket.create_connection((tar,int(port)))       
        while 1:  
                try:
                    mul_buf = mul_buf*2
                    junk = "A"*int(mul_buf)
                    sock.send(junk+'\r\n')
                    time.sleep(2)
                    if sock.recv(2000) == False:
                        raise Exception
                        return sock.shutdown(socket.SHUT_RDWR)
                        print "[+] Hoping its crash"
                        break
                    else:
                        print "[*] Trying buffer ",mul_buf
                        #print sock.recv(2000) 
                        continue
                #except Exception as e:
                 #   print e
                 #   print "[+] Crashed !!"
                 #   sock.close()
                 #   break
                except socket.error as msg:
                    print msg
                    print """
Stopped, Possible Reasons:
- Server not running
- port defined is not correct
- Hopefully you hit with a CRASH
                    """
                    sock.close()
                    break