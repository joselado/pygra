from gap import gap
import os

pwd = os.getcwd()
files = os.listdir(pwd+"/bands")

fo = open("phase3d.dat","w")

for f in files:
  os.system("cp bands/"+f+"  BANDS.OUT")
  l = f.split("_")
  mu = l[2]
  zee = l[4]
  g = gap()
  fo.write(str(mu)+"  "+str(zee)+"  "+str(g)+"\n")


fo.close()

