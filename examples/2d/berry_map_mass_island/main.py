# Add the root path of the pygra library
import os ; import sys ; sys.path.append(os.environ['PYGRAROOT'])

import numpy as np
from pygra import geometry
from pygra import hamiltonians
from pygra import specialgeometry
from pygra import topology
#raise # this does not work yet
g = geometry.honeycomb_lattice()
g = g.supercell(11)
h = g.get_hamiltonian(has_spin=False)
def fm(r): 
  if r.dot(r)<7.0: return 0.3
  else: return -0.3
h.add_sublattice_imbalance(fm)
topology.berry_green_map(h,k=[0.3333333,0.3333333,0.0],nrep=3,integral=True)
