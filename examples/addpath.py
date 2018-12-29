import os
ds = os.walk(os.getcwd())


def replace_line(l):
    """Fix imports in certain lines"""
    libs = ["geometry","hamiltonians","dos","kdos","scftypes"]
    if "# Add the root" in l: return ""
    for il in libs:
        if "import "+il in l and not "from pygra" in l:
            return "from pygra import "+il
    return l




def modify(ls):
    """Modify an input file to add the path"""
    ls = ls.split("\n") # split
    lo = "# Add the root path of the pygra library\n"
    lo += "import os ; import sys ; sys.path.append(os.environ['PYGRAROOT'])\n"
    lo += "\n"
    for l in ls: # loop over lines
      l = replace_line(l)
      if "import os" in l or "import sys" in l or "sys.path.append" in l: pass
      else: 
          if l!="": lo += l + "\n" # add line
    return lo

ds = [d[0] for d in ds] # loop

for d in ds:
  os.chdir(d) # go to that directory
  if os.path.isfile("main.py"):
      ls = open("main.py").read() # read all the lines
      print(d)
      open("main.py","w").write(modify(ls)) # write file
#  os.system("rm -f *.OUT")

