# Add the root path of the pygra library
import os ; import sys ; sys.path.append(os.environ['PYGRAROOT'])

import numpy as np
from pygra import geometry
from pygra import dos
g = geometry.hyperhoneycomb_lattice()
h = g.get_hamiltonian()
h.turn_dense()
h.get_bands()
exit()
h.turn_dense()
dos.autodos(h,nk=100,auto=True,delta=0.1,energies=np.linspace(-6.0,6.0,1000))
h.get_bands()
