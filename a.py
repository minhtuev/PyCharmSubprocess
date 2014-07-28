#!/usr/bin/env python
import subprocess

if __name__ == "__main__":
    print "Hey! I'm process A"
    proc = subprocess.call("ls")
    # this works
    # proc = subprocess.call(["/Users/minhtuevo/anaconda/bin/python", "/Users/minhtuevo/personal/PyCharmSubprocess/b.py"])
    # and this works too
    proc = subprocess.call(["python", "b.py"])
