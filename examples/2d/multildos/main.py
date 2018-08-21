
import sys
sys.path.append("../../../pygra")  # add pygra library

import geometry
import topology
import klist

g = geometry.honeycomb_lattice()
h = g.get_hamiltonian(has_spin=True)
import ldos
import numpy as np

ldos.multi_ldos(h,nk=4,es=np.linspace(-1,1,100),delta=0.1,nrep=3)
