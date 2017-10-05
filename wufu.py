#!/usr/bin/env python
import os,sys,cmd,re
from libs import FuzzClass
from libs.helpers import *
import imp

"""
====================
Main Engine of wufu 
====================
Every thing starts from here

Help:

banner            Reload/change banner
clear             clears the screen
execute           Execute a fuzzer/module
help              List available commands with "help" or detailed help with "help cmd".
info              Info on a fuzzer/module
main              Return to main
processes         Listing all process running
quit              quit wufu
reload            Reloading Module during development/glitch
search            Will search if module exists
set               Sets option for a fuzzer/module
show              Show fuzzers or options
use               Use a fuzzer/module
"""

class FuzzerMenu(cmd.Cmd):
    def __init__(self):
        cmd.Cmd.__init__(self)
        self.prompt = "wufu:fuzzers: > "
        self.doc_header = "Commands:"
        self.fuzz_control = FuzzClass.ControlFuzzer()
        self.fuzz_context = None
        self.mod_info = None
        self.mod_opts = None
    
    # Nice to have when we need it!
    def clear_context(self):
        print ("[!] Clearing Context")
        self.prompt = "wufu:fuzzers:"+self.fuzz_context+" > "
        self.fuzz_context = fuzz_context
        self.mod_info = None
        self.mod_opts = None        
    
    # lower case for everything
    def parseline(self, line):
        line = line.lower()
        return cmd.Cmd().parseline(line)    

    # show fuzzers, show info, show options
    def do_show(self, line):
        "Show fuzzers or options"
        if line == "fuzzers":
            self.fuzz_control.ListPathName()
        elif line == "options":
            if self.mod_opts == None:
                print ("You must use a fuzzer module first!")
                return
            print_opts(self.mod_opts)
        elif line == "info":
            if self.mod_info == None:
                print ("You must use a fuzzer module first!")
                return
            print_opts(self.mod_info)
        else:
            self.fuzz_control.ListPathName()

    def do_execute(self, line):
        "Execute a fuzzer/module"
        if self.fuzz_context == None:
            print ("use fuzzer/module first!")
            print ("set options next!")
        else:
            final_opts = self.fuzz_control.StripOpt(self.mod_opts)
            self.fuzz_control.LaunchFuzzer(self.fuzz_context, final_opts)
        print ("[!] Finished")
        self.clear_context() # finally....
    def do_banner(self,line):
        "Reload/change banner"
        banner()
    def do_main(self, line): # no reason if first class not used
        "Return to main"
        self.fuzz_context = None
        # exit cmdloop with True
        n = FuzzerMenu()
        n.cmdloop()
        #return True

    def do_clear(self, line):
        "clears the screen"
        screen()

    def do_quit(self, line):
        "quit wufu"
        print ("[!] Exiting WuFu")
        sys.exit(0)

    def do_use(self, line):
        "Use a fuzzer/module"
        # no need for "use fuzzers name" since already in fuzzers context
        path = os.getcwd() + "/libs/fuzzers/" # dunno if safe?
        modules = os.listdir(path) # dunno if safe?
        if line + ".py" in modules:
            self.prompt = "wufu:fuzzers:" + line + " > "
            self.fuzz_context = line
            self.mod_info, self.mod_opts = self.fuzz_control.ModuleSetting(self.fuzz_context) # easy way!
        else:
            print ("[-] Invalid Module/Fuzzer")
            
    def do_info(self, line):
        "Info on a fuzzer/module"
        if self.fuzz_context == None:
            print ("use fuzzer/module first!")
        else:
            print_info(self.mod_info)
            print_opts(self.mod_opts)

    def do_set(self, line):
        "Sets option for a fuzzer/module"
        if line == None:
            print ("info or show options to view correct param")
            return
        tmp_opt=line.split()
        if len(tmp_opt) < 2:
            print ("you must set a value with the option")
            return
        # return true if found, not really needed tho.. msf just sets then matches
        else:
                try:
                    self.fuzz_control.checkopt(tmp_opt[0],self.mod_opts)
                    bup = self.mod_opts[tmp_opt[0]]
                    bup[0] = tmp_opt[1]
                    self.mod_opts[tmp_opt[0]] = bup
                    print ("[!] %s  =>  %s" % (tmp_opt[0], self.mod_opts[tmp_opt[0]][0]))
                except Exception:
                    print "[-] No module Used"
                    return
    def do_processes(self,line):
        "Listing all process running"
        processes_list() 
    def do_search(self, line):
        "Will search if module exists"
        path = os.getcwd() + "/libs/fuzzers/" # dunno if safe?
        modules = os.listdir(path)
        print "Search Results"
        print "=============="
        for i in modules:
            if i.startswith(line):
                p = i.replace(".pyc","").replace(".py","")
                print p
    # This function yet to be worked upon... 
    def do_reload(self,line):
        "Reloading Module during development/glitch"
        module_source=os.getcwd()+"\\libs\\fuzzers\\"
        print module_source
        self.reload_all=imp.load_source(line,module_source)  
    
    # stolen from empire/recon-ng .. overwrite default cmd.Cmd().print_topics
    # right column is whats in quotes inside each do_command!
    def print_topics(self, header, cmds, cmdlen, maxcol):
        if cmds:
            self.stdout.write("%s\n" % str(header))
            if self.ruler:
                self.stdout.write("%s\n" % str(self.ruler * len(header)))
            for c in cmds:
                self.stdout.write("%s %s\n" % (c.ljust(17), getattr(self, 'do_' + c).__doc__))
            self.stdout.write("\n")

def set_readline():
        import readline,pyreadline
        #readline.parse_and_bind("tab: complete")
        readline.parse_and_bind('tab:complete')
        """
        if bind_exit_key("Control-c"):
            r = raw_input("[-] Exit wufu? y/n")
            while 1:
                    if r == 'y'or'yes':
                        print"[x] Exiting Wufu"    
                        sys.exit()
                    else:
                        n = FuzzerMenu()
                        n.cmdloop()"""
if __name__ == '__main__':
    banner()
    try :
        set_readline()
    except Exception :
        print "[-] Tab Auto-Complete Not Activated"
def start_wufu():    
    while 1:
            try:
                n = FuzzerMenu()
                n.cmdloop()
            except Exception as e:
                print "[-] Failed to start wufu. Possible Problem :"
                print e
            except KeyboardInterrupt as e:
                try:
                    choice = raw_input("\n Exit? [y/N] ")
                    if choice.lower() != "" and choice.lower()[0] == "y":
                            sys.exit()
                    else:
                        continue
                except KeyboardInterrupt as e:
                        continue
start_wufu()