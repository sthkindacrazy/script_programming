# -*- python3 -*-
""" Among information given after typing system info in Window cmd,
	this script will keep check memory, both real and virtual and
	record in a file """

import subprocess
import re
import time

filedirpath = "C:\\Desktop\\folder"

def checkMemory():
  systemres = subprocess.getoutput(["systeminfo"])
	# to get rid of , ex) 1,576 -> 1576
	systemres = systemres.replace(",", "")
	
	#use regex to pull out memories only
	pattern = re.compile('\d+MB')
	
	memorylist = pattern.findall(systemres)
