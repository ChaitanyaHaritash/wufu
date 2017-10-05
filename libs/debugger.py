"""
Debugger of Wufu
"""
from winappdbg import *
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
