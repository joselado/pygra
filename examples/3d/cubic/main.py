# Add the root path of the pygra library
import os ; import sys ; sys.path.append(os.environ['PYGRAROOT'])

import numpy as np
from pygra import geometry
from pygra import dos
g = geometry.cubic_lattice()
g.write()
h = g.get_hamiltonian()
# A well converged DOS requires more k-points
h.turn_dense()
h.get_bands()
dos.autodos(h,nk=100,auto=True,delta=0.1,energies=np.linspace(-6.0,6.0,1000))
