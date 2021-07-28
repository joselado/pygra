#!/usr/bin/python3
import os

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--m",default="Update",
        help='Message')

# overwrite the python libraries
os.system("rm -rf src/pygra") # remove
os.system("cp -r ../pyqula/src/pyqula src/pygra") # overwrite folder


args = parser.parse_args() # get the arguments

os.system("git add .")
os.system("git commit -m \"" + args.m+ "\"")
os.system("git push")
