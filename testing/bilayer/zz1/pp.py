from gap import gap
import os

pwd = os.getcwd()
files = os.listdir(pwd+"/bands")

for f in files:
  os.system("cp bands/"+f+"  BANDS.OUT")
  l = f.split("_")
  mu = l[1].split("=")[1]
  zee = l[2].split("=")[1]
  g = gap()
  os.system("tb90-bands -noshow")
  os.system("cp BANDS.png images/"+f+".png")
  print mu,zee,g
