# zigzag ribbon
import sys
sys.path.append("../../../pygra")  # add pygra library

import geometry
import topology
import numpy as np
import phasediagram
g = geometry.chain() # create geometry of a chain

def getz2(x1,x2): 
  # calculate the Z2 invariant for certain Zeeman and Rashba
  h = g.get_hamiltonian(has_spin=True) # get the Hamiltonian, spinfull
  h.add_rashba(0.5) # add Rashba SOC
  h.add_zeeman(x1+0.5) # add Zeeman field
  h.shift_fermi(2.0) # add Zeeman field
  h.add_swave(x2) # add swave pairing
  phi = topology.berry_phase(h) # get the berry phase
  return np.abs(phi/np.pi)

# now write the Phase diagram in a file
phasediagram.diagram2d(getz2,x=np.linspace(-1,1,20,endpoint=True),y=np.linspace(-1,2.,20,endpoint=True),nite=4)
