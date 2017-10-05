import random
from random import *
# huge thanks to g-laurent ;) ... all of this is his code.


class CoFuzz():
    def __init__(self, debugging=False):
        # self.debug = debugging
        self.DEBUG = debugging
        
    def intelli(self, packet):
        pack  = packet[:]
        byte = str(chr(choice(range(256))))
        pos = choice(range(len(packet)))
        pack[pos]= byte
        byte1 = choice(["\xff","\x80","\x41","\x00"])
        lon = randrange(0,8)
        pos2 = choice(range(len(packet)))
        pack[pos2]= byte1*lon
        if self.DEBUG: print ("Fuzzing intelli rand byte:[%s] pos:[%s] and comon:[%s] pos:[%s] len:[%s]\n" % (byte.encode("hex"),pos,byte1.encode("hex"),pos2,lon))
        return pack

    def onerand(self, packet):
        pack  = packet[:]
        byte = str(chr(choice(range(256))))
        pos = choice(range(len(packet)))
        pack[pos]= byte
        if self.DEBUG: print ("Fuzzing rand byte:[%s] Pos:[%s]\n" % (byte.encode("hex"),pos))
        return pack

    def doublerand(self, packet):
        pack  = packet[:]
        byte = str(chr(choice(range(256))))
        byte2 = str(chr(choice(range(256))))
        pos = choice(range(len(packet)))
        pos2 = choice(range(len(packet)))
        pack[pos]= byte
        pack[pos2]= byte2
        if self.DEBUG: print ("Fuzzing rand byte:[%s] pos:[%s], byte2:[%s] pos:[%s]\n" % (byte.encode("hex"),pos,byte2.encode("hex"),pos2))
        return pack

    def triplerand(self, packet):
        pack  = packet[:]
        byte = str(chr(choice(range(256))))
        byte2 = str(chr(choice(range(256))))
        byte3 = str(chr(choice(range(256))))
        pack[choice(range(len(packet)))]= byte
        pack[choice(range(len(packet)))]= byte2
        pack[choice(range(len(packet)))]= byte3
        if self.DEBUG: print ("fuzzing rand byte:%s byte2:%s byte3:%s\n" % (byte.encode("hex"),byte2.encode("hex"),byte3.encode("hex")))
        return pack

    def quadrand(self, packet):
        pack  = packet[:]
        byte = str(chr(choice(range(256))))
        byte2 = str(chr(choice(range(256))))
        byte3 = str(chr(choice(range(256))))
        byte4 = str(chr(choice(range(256))))
        pack[choice(range(len(packet)))]= byte
        pack[choice(range(len(packet)))]= byte2
        pack[choice(range(len(packet)))]= byte3
        pack[choice(range(len(packet)))]= byte4
        byte1 = choice(["\xff","\x80","\x41","\x00"])
        lon = randrange(0,8)
        pack[choice(range(len(packet)))]= byte1*lon
        if self.DEBUG: print ("fuzzing rand byte:%s byte2:%s byte3:%s byte4:%s\n" % (byte.encode("hex"),byte2.encode("hex"),byte3.encode("hex"),byte4.encode("hex")))
        return pack

    def longrand(self, packet):
        pack  = packet[:]
        byte = str(chr(choice(range(256))))
        lon = randrange(0,600)
        pos = choice(range(len(packet)))
        pack[pos]= byte*lon
        if self.DEBUG: print ("Fuzzing rand byte:[%s] pos:[%s-%s] len:[%s]\n" % (byte.encode("hex"),pos,(pos+lon),lon))
        return pack

    def longerrand(self, packet):
        pack  = packet[:]
        byte = str(chr(choice(range(256))))
        lon = randrange(0,5000)
        pos = choice(range(len(packet)))
        pack[pos]= byte*lon
        if self.DEBUG: print ("Fuzzing rand byte:[%s] pos:[%s-%s] len:[%s]\n" % (byte.encode("hex"),pos,(pos+lon),lon))
        return pack

    def longerrandnull(self, packet):
        pack  = packet[:]
        byte = str(chr(choice(range(256))))
        lon = randrange(0,1000) 
        pos = choice(range(len(packet)))
        pack[pos]= str(byte+"\x00")*lon
        if self.DEBUG: print ("Fuzzing rand byte:[%s] pos:[%s-%s] len:[%s]\n" % (byte.encode("hex"),pos,(pos+lon),lon))
        return pack

    def opnum(self, packet):
        pack  = packet[:]
        byte = str(chr(choice(range(0,2))))
        pos = choice(range(len(packet)))
        pack[pos]= byte
        if self.DEBUG: print ("Fuzzing opnum:[%s] pos:[%s]\n" % (byte.encode("hex"),pos))
        return pack

    def doubleopnum(self, packet):
        pack  = packet[:]
        byte = str(chr(choice(range(0,2))))
        byte2 = str(chr(choice(range(0,2))))
        pos = choice(range(len(packet)))
        pos2 = choice(range(len(packet)))
        pack[pos]= byte
        pack[pos2]= byte2
        if self.DEBUG: print ("Fuzzing opnum:[%s] pos:[%s] opnum2:[%s] pos[%s]\n" % (byte.encode("hex"),pos,byte2.encode("hex"),pos2))
        return pack

    def tripleopnum(self, packet):
        pack  = packet[:]
        byte = str(chr(choice(range(0,2))))
        byte2 = str(chr(choice(range(0,2))))
        byte3 = str(chr(choice(range(0,2))))
        pack[choice(range(len(packet)))]= byte
        pack[choice(range(len(packet)))]= byte2
        pack[choice(range(len(packet)))]= byte3
        if self.DEBUG: print ("fuzzing opnum:%s, opnum no-2:%s, opnum no-3:%s\n" % (byte.encode("hex"),byte2.encode("hex"),byte3.encode("hex")))
        return pack

    def doublenull(self, packet):
        pack  = packet[:]
        b = choice(range(len(packet)-2))
        c = b+2
        pack[b:c]= "\x00\x00"
        if self.DEBUG: print ("Fuzzing Doublenull pos:[%s] (\"\\x00\\x00\")\n" % (b))
        return pack

    def doubleff(self, packet):
        pack  = packet[:]
        b = choice(range(len(packet)-2))
        c = b+2
        pack[b:c]= "\xff\xff"
        if self.DEBUG: print ("Fuzzing Doubleff pos:[%s] (\"\\xFF\\xFF\")\n" % (b))
        return pack

    def doublera(self, packet):
        pack  = packet[:]
        b = choice(range(len(packet)-2))
        c = b+2
        byte = str(chr(choice(range(256))))
        pack[b:c]= byte*2
        if self.DEBUG: print ("Fuzzing Doublerand byte:[%s] pos:[%s]\n" % (byte.encode("hex"),b))
        return pack

    ###
    def remove1(self, packet):
        pack  = packet[:]
        i = randrange(0, len(pack)-1)
        b = pack[:i] + pack[i+1:]
        if self.DEBUG: print ("Remove char fuzz, removed:[%s] pos:[%s]\n"%(pack[i].encode("hex"),i))
        return b

    def changenull(self, packet):
        pack = packet[:]
        null = [i for i in range(len(pack)) if pack[i] == '\x00']
        byte = (chr(choice(range(256))))
        pack[choice(null)] = byte
        if self.DEBUG: print ("Replaced one null by:%s\n"% (byte.encode("hex")))
        return pack

    def changeff(self, packet):
        pack = packet[:]
        null = [i for i in range(len(pack)) if pack[i] == '\xff']
        byte = str(chr(choice(range(256))))
        pack[choice(null)] = byte
        if self.DEBUG: print ("Replaced one ff by a:%s\n" % (byte.encode("hex")))
        return pack

    def removenull(self, packet):
        pack = packet[:]
        null = [i for i in range(len(pack)) if pack[i] == '\x00']
        num = choice(null)
        del pack[choice(null)]
        if self.DEBUG: print ("Deleted null no-:%s\n"%(num))
        return pack
    ###

    def mspath(self, packet):
        pack  = packet[:]
        byte = choice(["O:\\ABC\\", "\\ABC", "O:ABC\\..\\XYZ", "O:ABC\\..\\..\\..\\/XYZ", "\\", "\\ABC\\XYZ", "/ABC/XYZ", "file:\\\\", "file:\\\\ABC", "file://ABC", "smb:\\\\", "smb:\\\\ABC", "\\ABC\\..\\..\\..", "ABC", "ABC\\XYZ", "\\\\SERVER\\ABC\\XYZ", "\\\\SERVER", "\\\\SERVER/ABC", "\\\\SERVER/XYZ", "\\\\SERVER/ABC\\..\\XYZ", "\\\\SERVER\\\../ABC/XYZ", "\\\\SERVER/ABC\\..\\XYZ\\../HI", "\\\\.\\", "\\\\.\\ABC", "\\\\.\\pipe\\ABC", "\\\\.\\X:\\ABC\\XYZ", "\\\\.\\X:\\ABC\\..\\XYZ", "\\\\.\\X:\\ABC\\..\\..\\O:\\ABC", "\\\\.\\X:\\ABC\\..\\..\\\\.\\localhost\\XYZ", "\\\\.\\X:\\ABC\\..\\..\\", "\\\\.\\pipe\\ABC\\..\\XYZ", "\\\\.\\pipe\\ABC", "\\\\²\\ABC", "\\\\.\\ABC²\\XYZ", "\\\\?\\X:\\ABC", "\\\\?\\X:\\ABC\\XYZ", "\\\\?\\X:\\ABC\\XYZ\\..\\..\\", "\\\\?\\X:/ABC/XYZ", "\\\\?\\X:\\ABC\\..\\XYZ", "\\\\??\\pipe\\ABC\\..\\XYZ", "\\\\??\\pipe\\ABC", "\\\\²\\ABC", "\\\\??\\ABC²\\XYZ", "\\\\??\\X:\\ABC", "\\\\??\\X:\\ABC\\XYZ", "\\\\??\\X:\\ABC\\XYZ\\..\\..\\", "\\\\??\\X:/ABC/XYZ", "\\\\??\\X:\\ABC\\..\\XYZ"])
        # byte = choice(["\\a\\..\\.",".\\a\\","./a/","a$",".\\a\\..",".\\...\\aaa\\\\.."])
        lon = randrange(0,400)
        pos = choice(range(len(packet)))
        pack[pos]= str(byte*lon)
        if self.DEBUG: print ("Fuzzing chosen str:[%s] pos:[%s] len:[%s]\n" % (byte.encode("hex"),pos,lon))
        return pack

    def common(self, packet):
        pack  = packet[:]
        byte = choice(["\xff","\x80","\x41","\x00"])
        lon = randrange(1,8)
        pos = choice(range(len(packet)))
        b = pos-lon
        c = b+lon
        pack[b:c]= byte*lon
        if self.DEBUG: print ("Fuzzing common rand common byte:[%s] pos:[%s] len:[%s]\n" % (byte.encode("hex"),pos,lon))
        return pack

    def addsome(self, packet):
        pack  = packet[:]
        i = "\x00" * randrange(0, 50)
        pos = choice(range(len(packet)))
        pack[pos] = i
        if self.DEBUG: print ("Added null char pos:[%s-%s] len:[%s]\n"%(pos,(pos+len(i)),len(i)))
        return pack

    def removesome(self, packet):
        pack  = packet[:]
        i = randrange(0, len(pack)-1)
        b = pack[:i] + pack[i+randrange(0, len(pack)-1):]
        if self.DEBUG: print ("Remove some char fuzz, removed byte:[%s]\n"%(pack[i].encode("hex")))
        return b

    def overflow(self, packet):
        pack = packet[:]
        lon = choice([50, 100, 300, 500, 750, 1000, 2000, 4000, 5000, 10000, 20000, 50000])
        pos = choice(range(len(packet)))
        pack[pos] = '\x41'*lon
        if self.DEBUG: print ("Fuzzing overflow pos:[%s-%s] with [%s]:A's\n" % (pos,(pos+lon),lon))
        return pack

    # 50% of the time
    def generate():
        return random.random() <= 0.50
    
# Make a normal packet then do this
# packet = "\x01\x02\x03\x04\x05\x06\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f"    #<-- normal packet
# fuzz_it = [i for i in packet]
# fuzz = CoFuzz(True)    # True for debugging
# fuzzed = ''.join(fuzz.overflow(fuzz_it))
