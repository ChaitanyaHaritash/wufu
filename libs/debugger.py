"""
Debugger of Wufu
"""
from winappdbg import *
import sqlalchemy
debug = Debug()
def Attach_to_Process_Name(process_name):
	"Attaching to process by name"
	try:
		for process , name in debug.system.find_processes_by_filename(process_name):
			print "[*] Trying attach to process ",process.get_pid(),process_name
			debug.attach(process.get_pid())
		#debug.loop()
	finally:
		debug.stop()
def Attach_via_PID(pid):
	"""
	Attach to process by its PID, you can use command processes to list all running processes
	to get process id.
	"""

	try:
		try:
			print "[*] Trying to attach to ",pid
			debug.attach(pid)
			print "[*] Attaching Complete"
		except Exception as e:
			print "[*] Unable to attach to process ",pid
			print e
	except Exception as e:
		print "[!] Please clear issue/s first"
		print e
	finally:
		debug.stop()




def handler(event):
    name = event.get_event_name()
    code = event.get_event_code()
    pid = event.get_pid()
    tid = event.get_tid()
    #pc = get the value of eip
    pc = event.get_thread().get_pc()
    bits = event.get_process().get_bits()
    format_string = "%s (%s) at address = %s, process %d, thread %d"
    message = format_string % ( name,
                                HexDump.integer(code, bits),
                                HexDump.address(pc, bits),
                                pid,
                                tid )

    print message
    #if crast happens
    if code == win32.EXCEPTION_DEBUG_EVENT and event.is_last_chance():
            print("crash occured,storing crash dump....")
            crash = Crash(event)
            crash.fetch_extra_data(event,takeMemorySnapshot = 2)
            #takeMemorySnapshot = 0 means no memory dump
            #takeMemorySnapshot = 1 means small memory dump
            #takeMemorySnapshot = 2 means full memory dump
            store_dump = CrashDAO( "sqlite:///crashes.sqlite" )
            store_dump.add(crash)
            event.get_process().kill()


