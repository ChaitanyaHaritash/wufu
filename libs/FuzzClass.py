#!/usr/bin/env python
import os
from fuzzers import *
import importlib

#this class manages all fuzzers actions
class ControlFuzzer():
    def __init__(self):
        self.NothingHere = None # "class storage.. use it!"
    # list all modules available
    def ListPathName(self):
        self.path = os.getcwd()
        mod_dir="fuzzers/"
        dirs = self.path+"/libs/"+mod_dir
        self.modules = os.listdir(dirs)
        print ("")
        print ("Available Fuzzers:")
        print ("==================")
        for i in self.modules:
            if i.endswith(".py"):
                p_fuz = i.replace(".py","").replace("__init__","")
                if ("template" in p_fuz):
                    r = p_fuz.replace("template","")
                    print r 
                else:
                    print (p_fuz)
    # shows info about module, like author,name,description and options it requires 
    def ModuleSetting(self,fuzzer_name):
        # all of this is REALLY BAD!
        self.path = os.getcwd()
        mod_dir="fuzzers/"
        dirs = self.path + "/libs/" + mod_dir
        self.modules = os.listdir(dirs)
        load_fuzz=dirs + fuzzer_name + ".py"
        runner = "libs.fuzzers."+fuzzer_name
        method = importlib.import_module(runner)
        return method.ModuleFuzzer().info, method.ModuleFuzzer().opts

    #Executes module loaded, this func will be passed to fuzzsetlaunch class
    def LaunchFuzzer(self, fuzzer_name, options):
        try:    
            runner = "libs.fuzzers." + fuzzer_name
            method = importlib.import_module(runner)
            method.ModuleFuzzer().executer(options)
        except KeyboardInterrupt:
            print ("[-] Keyboard Interrupt Raised, Quitting")
            pass

    # Checks to make sure all required options are set... 
    # this should never err as we define them with "fake" values
    def CheckRequired(self, opt):
        for key, val in opt.items():
            if val[1] == True:
                if val[0] == None or val[0] == False:
                    return True
    
    # input a dict like.. { 'target': ["127.0.0.1", True, "The IP to target"] }
    # and returns { 'target': '127.0.0.1' }
    # you must still set correct data type in module
    def StripOpt(self, opt):
        if self.CheckRequired(opt):
            print ("All required options are not set!!!")
            print ("This is going to cause you issues!!")
        ret = {}
        for key, val in opt.items():
            ret[key] = val[0]
        return ret
        
        
    # this func will check if valid options are being set and exists
    # this func will be passed to fuzzsetlaunch class   
    def checkopt(self, in_opt, mod_opts):
        for key, val in mod_opts.items():
            if in_opt in key:
                return True
        return False