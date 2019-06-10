# Add the root path of the pygra library
import os ; import sys ; sys.path.append(os.environ['PYGRAROOT'])

# zigzag ribbon
import numpy as np
from pygra import geometry
from pygra import scftypes
from scipy.sparse import csc_matrix
g = geometry.honeycomb_lattice()
g = g.supercell(9)
h = g.get_hamiltonian() # create hamiltonian of the system
mf = scftypes.guess(h,mode="antiferro")
U = 3.0
scf = scftypes.selfconsistency(h,nkp=1,filling=0.5,g=U,
              mix=0.9,mf=mf,mode="U")
h = scf.hamiltonian # get the Hamiltonian
h.write_magnetization()
h.get_bands() # calculate band structure
