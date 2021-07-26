# Add the root path of the pygra library
import os ; import sys 
sys.path.append(os.path.dirname(os.path.realpath(__file__))+"/../../../src")





import numpy as np
from pygra import geometry
from pygra import groundstate
g = geometry.honeycomb_lattice()
g = g.supercell(3)
g.dimensionality = 0
h = g.get_hamiltonian(has_spin=False) # create hamiltonian of the system
filling = 0.5

from pygra.selfconsistency import densitydensity
#scf = scftypes.selfconsistency(h,nk=nk,filling=filling,g=g,mode="V")
scf = densitydensity.Vinteraction(h,V1=2.0,V2=1.0,filling=filling)
h = scf.hamiltonian # get the Hamiltonian
h.get_bands() # calculate band structure
from pygra import topology
groundstate.hopping(h)
topology.write_berry(h)






