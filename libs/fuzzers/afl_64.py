#!/usr/bin/env python

import socket,time,platform
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
                    'target'         : ['',           True,  'Path to target binary'],
                    'test_case_path' : ['',           True,  'Path to directory with test cases'],
                    'result_dir'     : ['',           True,  'Path to directory to save results'],
                    'timeout'        : ['',           True,  'Timeout for each run']
                })

        self.info = {
                    'Name'             : '64-Bit AFL Fuzzer',
                    'Description'      : '64-Bit AFL Fuzzer, Mutation fuzzer',
                    'Author'           : '@bofheaded'
                }

    def executer(self, option):
        self.arch = windows_arch32_check()
        print "[*] Executing AFL, Press CTRL+C to halt execution"
        target = option['target']
        test_path=option['test_case_path']
        results=option['result_dir']
        timeout=option['timeout']
        dest="\\utils\\fuzzers\\AFL_64\\"
        self.path = os.getcwd()+dest
        #afl-fuzz.exe -i in -o out -D C:\work\winafl\DynamoRIO\bin64 -t 20000 ---coverage_module gdiplus.dll -coverage_module WindowsCodecs.dll --fuzz_iterations 5000 -target_module test_gdiplus.exe -target_offset 0x1270 --nargs 2 -- test_gdiplus.exe
        os.system(str(self.path)+"afl-fuzz.exe"+" -i "+test_path+" -o "+results+" -D "+self.path+" -t "+timeout+" ---coverage_module gdiplus.dll -coverage_module WindowsCodecs.dll --fuzz_iterations 5000 -target_module test_gdiplus.exe -target_method main -nargs 2 --test_gdiplus.exe "+target )
        
    
