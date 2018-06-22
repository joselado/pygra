# zigzag ribbon
import sys
import os


sys.path.append("../../../pygra")  # add pygra library

import numpy as np
import geometry
import scftypes
import operators
from scipy.sparse import csc_matrix
g = geometry.honeycomb_lattice()
g.write()


Us = np.linspace(0.,4.,10) # different Us

#Us = [2.,4.]
#Us = [2.]

f = open("EVOLUTION.OUT","w") # file with the results

for U in Us: # loop over Us
#  import scftypes
  
  h = g.get_hamiltonian() # create hamiltonian of the system
  h = h.get_multicell()
  
  h.shift_fermi(0.0)
  
  
  mf = scftypes.guess(h,mode="antiferro")
  scf = scftypes.selfconsistency(h,nkp=10,filling=0.5,g=U,
                mix=0.9,mf=mf,mode="U")
  h = scf.hamiltonian # get the Hamiltonian
#  h.get_bands() # calculate band structure
  print(scf.interactions[0].g) 
  print(len(scf.interactions)) 
#  import groundstate
  f.write(str(U)+"   "+str(scf.gap)+"\n")
#  groundstate.swave(h)
  #groundstate.hopping(h)
  
f.close()

