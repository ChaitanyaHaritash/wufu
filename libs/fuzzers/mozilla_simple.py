#!/usr/bin/env python

import time,os
# from collections import OrderedDict # needed for options to be in order!
from libs.fuzzers import *
from collections import OrderedDict
# you can import directly from higher dir?
from libs.helpers import *
from libs.debugger import *

""" this fuzzer module is meant to work with WuFu only """ 

# we need to set a base standard for making modules... 
class ModuleFuzzer():
    # no need for global.. use __init__ and self :]
    def __init__(self):
        # self.opts = OrderedDict({ 
        #  not sure why OrdDict isnt working.. leaving for now as it doesnt afffect much
        self.opts = OrderedDict({
                    # all opts must be lower fyi...
                    'initial_multiple'         : [int(5000),         True,  'Initial multiply'],
                    'increment'                : [int(50),           True,  'Increment'],
                    'pid'                      : [None,              True,  'Process PID']
                })

        self.info = {
                    'Name'             : 'Simple Mozilla Firefox Fuzzer',
                    'Description'      : 'Simple Browser fuzzer, opens js code embed file into browser with string increment',
                    'Author'           : '@bofheaded'
                }

    def get_set(self,option):
        init = option['initial_multiple']
        inic = option['increment']
        ince = 0
        global path
        path = os.getcwd() + "\\utils\\fuzzers\\browsers\\mozilla\\simple\\" 
        while 1 :
            with open(path+"test.html","w+") as f:
                    #print "[!] Trying with => %s"%dope 
                    ince += 1
                    inje = ince +int(inic)
                    dope = int(init) * int(inje)
                    print "[!] Trying with => %s"%dope
                    payload = """
<html>
<head></head>
<body>
<script>
function done() {
}
         
var x = '';
for (i=0; i<"""+str(dope)+"""; ++i)
x += '<a>';
var uri = 'data:image/svg+xml,' + x;
var i = new Image();
i.src = uri;
</script>
</body>
</html>
                """
                    f.write(payload)
            time.sleep(5)
    def executer(self, option):
        pid = option['pid']
        #self.get_set(option=option)
        process_name="firefox.exe"
        #Attach_to_Process(process_name=process_name)
        Attach_via_PID(pid=int(pid))    