#!/usr/bin/env python

"""
TEMPLATE for WuFu
"""

# Standard Python Libs
import time,os
from collections import OrderedDict
# Wufu Libs
from libs.helpers import *
from libs.debugger import *
from libs.fuzzers import *

""" this fuzzer module is meant to work with WuFu only """ 

# we need to set a base standard for making modules... 
class ModuleFuzzer():
    def __init__(self):
        self.opts = OrderedDict({
                    # all opts must be lower fyi...
                    'option 1'         : ["initial value",         True,  'Description of value'],
                    'option 2'         : ["initial value",         True,  'Description of value'],
                    'Option 3'         : ["initial value",         True,  'Description of value']
                })

        self.info = {
                    'Name'             : 'Name of Module/fuzzer',
                    'Description'      : 'Description about Module/fuzzer',
                    'Author'           : 'Author Name'
                }

# Standard function to be mentioned in every module/fuzzer
# As it will execute main code  
    def executer(self, option):
        print "lemme execute it :)"