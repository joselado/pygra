# Add the root path of the pygra library
import os ; import sys ; sys.path.append(os.environ['PYGRAROOT'])

# zigzag ribbon
import numpy as np
from pygra import geometry
from scipy.sparse import csc_matrix
from pygra import meanfield
g = geometry.honeycomb_lattice()
#g = geometry.kagome_lattice()
g = g.supercell(1)
filling = 0.5
nk = 10
h = g.get_hamiltonian(has_spin=False) # create hamiltonian of the system
#scf = scftypes.selfconsistency(h,nk=nk,filling=filling,g=g,mode="V")
scf = meanfield.Vinteraction(h,V2=1.0,nk=nk,filling=filling)
from pygra import scftypes
#scf = meanfield.hubbardscf(h,U=2.6,nk=nk,filling=filling)
#scf = scftypes.hubbardscf(h,U=2.6,nk=nk,filling=filling)

h = scf.hamiltonian # get the Hamiltonian
h.get_bands() # calculate band structure
from pygra import groundstate
groundstate.hopping(h,nrep=3) # write three replicas
#spectrum.fermi_surface(h)
