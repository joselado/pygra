# zigzag ribbon
import sys
import os


sys.path.append("../../../pygra")  # add pygra library

import numpy as np
import geometry
import scftypes
from scipy.sparse import csc_matrix
g = geometry.honeycomb_lattice()
h = g.get_hamiltonian() # create hamiltonian of the system
mf = scftypes.guess(h,mode="antiferro")
U = 3.0
scf = scftypes.selfconsistency(h,nkp=10,filling=0.5,g=U,
              mix=0.9,mf=mf,mode="U")
h = scf.hamiltonian # get the Hamiltonian
h.write_magnetization()
h.get_bands() # calculate band structure
