
import numpy as np
import os
from gap import gap
mus = np.arange(0.1,0.6,0.05)
zees = np.arange(0.0,0.3,0.03)

f = open("map.dat","a")

for mu in mus: # loop over parameters
  for zee in zees:
    os.system("python main.py  "+str(zee)+"  "+str(mu))
    os.system("tb90.x")
    os.system("cp BANDS.OUT bands/BANDS.OUT_mu="+str(mu)+"_zee="+str(zee))
    g = gap()
    f.write(str(mu)+"  "+str(zee)+"  "+str(g)+"\n")
    print mu,zee,g
f.close()
 
