from PyDAQmx.DAQmxFunctions import *

def getDeviceName():
	a = create_string_buffer(1024)
	# Buffer will break if too many devices, like 10 or 15, make number 100 bigger if you have to
	b = c_ulong(1024)
	DAQmxGetSysDevNames(a, b)
	return a.value.decode('utf-8').split(',')[-1].strip()