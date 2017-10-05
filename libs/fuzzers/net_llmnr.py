#!/usr/bin/env python

import socket, struct, binascii
from collections import OrderedDict
from libs.helpers import *

class ModuleFuzzer():
    " This fuzzer module is meant to work with WuFu only"
    def __init__(self):
        self.opts = OrderedDict({
                    # all opts must be lower fyi...
                    'respondip'  : ['127.0.0.1',           True,  'Target IP Address'],
                    'port'       : ['5355',                True,  'Port on which service is running'],
                    'mcastip'    : ['224.0.0.252',         True,  'The multicast IP to use'],
                    'mcastport'  : ['5535',                True,  'The multicast PORT to use'],
                })

        self.info = {
                    'Name'             : 'Simple LLMNR Fuzzer',
                    'Description'      : 'Listens on multicat "224.0.0.252" and responds with a fuzzed packet.',
                    'Author'           : '@vvalien'
                }

    # I Dont this this works actually... but no way to test......
    def setup_listener(self, option):
        # this was a real pain in the dick to figure out back then...
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # bind to multicast ip and port
        sock.bind(('', int(option["mcastport"])))
        # I Dont this this works actually... but no way to test......
        mreq = struct.pack("4sl", socket.inet_aton(option["mcastip"]), socket.INADDR_ANY)
        sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)
        return sock
        
    # trusty packet construct
    def pakit(self, transid, rname, respip):
        ret = transid                 # ret transact ID
        ret += '\x80\00'              # quary response
        ret += '\x00\x01'             # questions = 16
        ret += '\x00\x01'             # anser RRs = 16
        ret += '\x00\x00'
        ret += '\x00\x00'
        ret += struct.pack(">h",len(rname))[1]
        ret += rname
        ret += '\x00'                 # null?
        ret += '\x00\x01'             # type
        ret += '\x00\x01'             # class
        ret += struct.pack(">h",len(rname))[1] # has to have this
        ret += rname
        ret += '\x00'                 # null?
        ret += '\x00\x01'             # Type
        ret += '\x00\x01'             # class # 01 = IN
        ret += '\x00\x00\x00\x1e'     # poison time 30sec
        ret += '\x00\x04'             # IP len ???
        ret += socket.inet_aton(respip)
        return ret
        
    # parse the sequence num, name, and quary type A or AAAA
    def parse_llmnr(self, data):
        NameLen = struct.unpack('>B',data[12])[0]
        Name = data[13:13+NameLen]
        Tid=data[0:2]
        Typ=data[len(data)-4:len(data)-2]
        return Name, Tid, Typ
    
    def executer(self, option):
        try:
            print ("[!] Executing fuzzer...")
            sock = self.setup_listener(option)
            # get a packet
            pkt, ip = sock.recvfrom(1024)
            if pkt != '':
                # parse the name and transact ID
                nam, tid, typ = self.parse_llmnr(pkt)
                if typ == '\x00\x01': # type A
                    ret = self.pakit(tid, nam, option["respondip"])
                    ### INSERT FUZZLIB HERE ####
                    sock.sendto(ret, (ip[0], ip[1]))
                    # print the hex of everything
                    print binascii.hexlify(tid), nam, binascii.hexlify(pkt)
        except Exception as e:
            print (e)