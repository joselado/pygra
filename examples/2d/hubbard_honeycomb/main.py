# zigzag ribbon
import sys
import os


sys.path.append(os.environ["PYGRAROOT"])  # add pygra library

import numpy as np
import geometry
import scftypes
import operators
from scipy.sparse import csc_matrix
g = geometry.honeycomb_lattice()
g.write()


Us = np.linspace(0.,4.,10) # different Us

f = open("EVOLUTION.OUT","w") # file with the results

for U in Us: # loop over Us
#  import scftypes
  
  h = g.get_hamiltonian() # create hamiltonian of the system
#  h = h.get_multicell()
  
#  h.shift_fermi(0.0)
  
  
  mf = scftypes.guess(h,mode="antiferro")
  scf = scftypes.selfconsistency(h,nkp=20,filling=0.5,g=U,
                mix=0.9,mf=mf,mode="U",broyden=True)
  h = scf.hamiltonian # get the Hamiltonian
#  h.get_bands() # calculate band structure
#  import groundstate
  gap = h.get_gap()
  f.write(str(U)+"   "+str(gap)+"\n")
#  groundstate.swave(h)
  #groundstate.hopping(h)
  
f.close()

