import subprocess
import re
import time

filedirpath = "C:\\Desktop"

def checkMemory():
    systemres = subprocess.getoutput(["systeminfo"])
