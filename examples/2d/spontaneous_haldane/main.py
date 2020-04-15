# Add the root path of the pygra library
import os ; import sys ; sys.path.append(os.environ['PYGRAROOT'])

import numpy as np
from pygra import geometry
from pygra import groundstate
g = geometry.honeycomb_lattice()
h = g.get_hamiltonian(has_spin=False) # create hamiltonian of the system
nk = 10
filling = 0.5
g = 2.0 # interaction

from pygra.selfconsistency import densitydensity
#scf = scftypes.selfconsistency(h,nk=nk,filling=filling,g=g,mode="V")
scf = densitydensity.Vinteraction(h,V1=0.0,V2=g,nk=nk,filling=filling)
h = scf.hamiltonian # get the Hamiltonian
h.get_bands() # calculate band structure
from pygra import topology
groundstate.hopping(h)
topology.write_berry(h)
