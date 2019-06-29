# Add the root path of the pygra library
import os ; import sys ; sys.path.append(os.environ['PYGRAROOT'])

# zigzag ribbon
import numpy as np
from pygra import geometry
from pygra import scftypes
from pygra import operators
from scipy.sparse import csc_matrix
g = geometry.honeycomb_lattice()
#g = geometry.bichain()
#g = g.supercell(3)
#g = geometry.triangular_lattice()
#g = g.supercell(3)
h = g.get_hamiltonian(has_spin=False) # create hamiltonian of the system
h = h.get_multicell()
mf = scftypes.guess(h,mode="CDW",fun=1.0) 
scf = scftypes.selfconsistency(h,nkp=100,filling=0.5,g=10.0,
                mix=0.9,mf=mf,mode="Coulomb")
h = scf.hamiltonian
h.write_onsite()
h.get_bands()
print(h.extract("density"))
