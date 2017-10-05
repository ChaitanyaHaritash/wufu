import os
import banners
from winappdbg import System
system = System()
def check_root_nux():
    if os.geteuid==0:
        print "[!] WuFu needs root privileges" 
        sys.exit()
    else:
        pass
def screen():
    if os.name == "posix":  
        check_root_nux()
        os.system("clear")
    else :
        os.system("cls")
def banner():
    screen()    
    x = banners.BannerLoad()
    x.bannerloder()
    print " Release Status => BETA"
    #print ""
    print "==============================="
    print """[Twitter:] @bofheaded @vvalien1"""
    print "==============================="
    print ""
def windows_arch32_check():
    if "ProgramFiles(x86)" in os.environ:
        print "[*] Architecture is x64"
    else:
        print "[*] Architecture is x86"      
# ALWAYS () wrap print .. also format for complex data
def print_info(info):
    print ("")
    print ("    Module Info:")
    print ("    ===============================================")        
    for des in info:
        print ("    %s : %s" % ("{0: <15}".format(des), "{0: <17}".format(info[des])))
    print ("")
def processes_list():
    print ""
    print "PID     Process Name"
    print "----------------------------------------------------------"
    print ""
    for process in system:
        print "%d:\t%s" % ( process.get_pid(), process.get_filename() )
def print_opts(opts):
    #print ("\n")
    #print ("   Module Options:")
    #print ("   ===============================================")
    #print ("")
    
    # I like the above but this I think looks better?
    ln = "="
    print("    %s  %s  %s  %s" % ("{0: <15}".format("Name"), "{0: <22}".format("Current Setting"), "{0: <11}".format("Required"), "{0: <30}".format("Description")))
    print("    %s  %s  %s  %s" % ("{0: <15}".format(ln*14), "{0: <22}".format(ln*22), "{0: <11}".format(ln*11), "{0: <30}".format(ln*30)))
    for key, val in opts.items():
        print("    %s  %s  %s  %s" % ("{0: <15}".format(key), "{0: <22}".format(val[0]), "{0: <11}".format(str(val[1])), "{0: <30}".format(val[2])))
    print ("")