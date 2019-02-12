# Add the root path of the pygra library
import os ; import sys ; sys.path.append(os.environ['PYGRAROOT'])

# zigzag ribbon
import numpy as np
from pygra import geometry
from pygra import scftypes
from pygra import operators
from scipy.sparse import csc_matrix
g = geometry.honeycomb_lattice()
h = g.get_hamiltonian() # create hamiltonian of the system
h.add_anti_kane_mele(0.1)
mf = scftypes.guess(h,mode="random") # antiferro initialization
# perform SCF with specialized routine for Hubbard
U = 3.0
scf = scftypes.hubbardscf(h,nkp=10,filling=0.5,g=U,
              mix=0.9,mf=mf)
scf.hamiltonian.get_bands(operator="sz")
