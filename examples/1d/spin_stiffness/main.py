# zigzag ribbon
import sys
sys.path.append("../../../pygra")  # add pygra library

import geometry
import scftypes
import numpy as np


# this spin calculates the spin stiffness of an interacting 1d chain


g = geometry.chain() # chain geometry
h0 = g.get_hamiltonian() # create hamiltonian of the system

fo = open("STIFFNESS.OUT","w") # open file


for a in np.linspace(0.,.2,20): # loop over angles, in units of pi
  h = h0.copy()
  h.generate_spin_spiral(angle=a,vector=[0.,1.,0.])
  scf = scftypes.hubbardscf(h,filling=0.1,nkp=1000,U=2.5,silent=True,
           mag=[[0.,0.,.1]],mix=0.01,maxerror=1e-4)
  fo.write(str(a)+"    "+str(scf.energy)+"\n") # write
  print(a,scf.energy)

fo.close()
