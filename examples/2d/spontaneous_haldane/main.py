# Add the root path of the pygra library
import os ; import sys ; sys.path.append(os.environ['PYGRAROOT'])

import numpy as np
from pygra import geometry
from pygra import groundstate
from pygra import meanfield
g = geometry.honeycomb_lattice()
h = g.get_hamiltonian(has_spin=False) # create hamiltonian of the system
nk = 10
filling = 0.5

#scf = scftypes.selfconsistency(h,nk=nk,filling=filling,g=g,mode="V")
mf = meanfield.guess(h,"Haldane") # initialization
scf = meanfield.Vinteraction(h,mf=mf,V2=1.0,nk=nk,filling=filling,mix=0.1)
h = scf.hamiltonian # get the Hamiltonian
h.get_bands() # calculate band structure
from pygra import topology
groundstate.hopping(h)
topology.write_berry(h)
