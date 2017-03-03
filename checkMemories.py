# -*- python3 -*-
""" Among information given after typing system info in window cmd,
    this script will keep check memory, both real and virtual and
    record collected info in a file """

import subprocess
import re
import time

filedirpath = "C:\\Desktop\\folder\\"
filewriteform = "memory0: %s memory1: %s memory2: %s memory3: %s memory4: %s\n"

def checkMemory():
    systemres = subprocess.getoutput(["systeminfo"])
    #to get rid of , ex) 1,576 -> 1576
    systemres = systemres.replace(",", "")
    
    #use regex to pull out memories only
    pattern = re.compile('\d+MB')
    memorylist = pattern.findall(systemres)
    
    #recent comes first
    filepath = filedirpath+"record_systeminfo.txt"
    with open(filepath, "r") as readfile:
        priordata = readfile.read()
    with open(filepath, "w") as writefile:
        writefile.write(filewriteform % 
                        (memorylist[0],memorylist[1],memorylist[2],memorylist[3],memorylist[4]) + priordata)
    
    #one hour base
    time.sleep(60*60)
