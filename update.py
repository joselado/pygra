#!/usr/bin/python3
import os

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--m",default="Update",
        help='Message')

path = os.path.dirname(os.path.realpath(__file__)) # real path
os.chdir(path) # go to the home folder

# overwrite the python libraries with the pyqula version
# (this is for short term compatibility)
os.system("rm -rf src/pygra") # remove
os.system("cp -r ../pyqula/src/pyqula src/pygra") # overwrite folder


args = parser.parse_args() # get the arguments

os.system("git add .")
os.system("git commit -m \"" + args.m+ "\"")
os.system("git push")
