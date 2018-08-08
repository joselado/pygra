
import numpy as np
import os
from gap import gap
mus = np.arange(0.0,0.1,0.005)
zees = np.arange(0.0,0.3,0.01)


# create a folder for darwin
os.system("rm -r inputs")
os.system("mkdir inputs")

for mu in mus: # loop over parameters
  for zee in zees:
    fol = "inputs/zee_"+str(zee)+"_mu_"+str(mu)
    os.system("python main.py  "+str(zee)+"  "+str(mu))
    os.system("mkdir "+fol)
    os.system("cp hamiltonian.in "+fol)
    os.system("cp operator.in "+fol)
 
