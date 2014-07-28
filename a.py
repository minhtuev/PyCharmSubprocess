#!/usr/bin/env python
import subprocess

if __name__ == "__main__":
    print "Hey! I'm process A"
    proc = subprocess.call("ls")
    proc = subprocess.Popen("python b.py", shell=True).communicate()