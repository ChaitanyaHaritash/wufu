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
                    'buffer'  : ['100',                 True,  'Maximum Buffer Size'],
                    'username': [None,                  False, 'The Username'],
                    'password': [None,                  False, 'The Password']
                })

        self.info = {
                    'Name'             : 'Simple FTP Fuzzer',
                    'Description'      : 'Simple FTP Fuzzer, sends defined multiple of a string to desired ftp target server',
                    'Author'           : '@bofheaded'
                }

    def executer(self, option):
        print ("[!] Executing fuzzer on %s:%s" % (option["target"], option["port"]))
        buf = option["buffer"]
        tar = option['target']
        port = option['port']
        usern = option['username']
        pas = option['password']
        sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        junk = "\x41"*int(buf)
        
        if pas and usern != None:
            print "go for it"
        else:        
                try:
                    sock.connect((tar,int(port)))
                    print ""
                    print "Server Response :"
                    print sock.recv(2000)
                    sock.send(junk+"\r\n")
                except Exception as e:
                    print e
                finally:
                    sock.close()