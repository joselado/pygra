# Add the root path of the pygra library
import os ; import sys ; sys.path.append(os.environ['PYGRAROOT'])

# zigzag ribbon
import numpy as np
from pygra import geometry
from scipy.sparse import csc_matrix
from pygra import meanfield
g = geometry.honeycomb_lattice_C6()
g = geometry.honeycomb_lattice()
g = g.supercell(3)
filling = 0.5
nk = 10
h = g.get_hamiltonian(has_spin=False) # create hamiltonian of the system
#scf = scftypes.selfconsistency(h,nk=nk,filling=filling,g=g,mode="V")
mf = meanfield.guess(h,"kekule")
#mf = None
scf = meanfield.Vinteraction(h,V1=6.0,mf=mf,
        V2=4.0,nk=nk,filling=filling,mix=0.3)
h = scf.hamiltonian # get the Hamiltonian
h.get_bands(operator="valley") # calculate band structure
from pygra import groundstate
groundstate.hopping(h,nrep=3) # write three replicas
h.write_onsite(nrep=3) # write three replicas
#spectrum.fermi_surface(h)
