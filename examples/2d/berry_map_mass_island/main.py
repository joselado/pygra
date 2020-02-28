# Add the root path of the pygra library
import os ; import sys ; sys.path.append(os.environ['PYGRAROOT'])

import numpy as np
from pygra import geometry
from pygra import hamiltonians
from pygra import specialgeometry
from pygra import topology
#raise # this does not work yet
g = geometry.honeycomb_lattice()
g = g.supercell(12)
h = g.get_hamiltonian(has_spin=False)
rmax = np.sqrt(g.a1.dot(g.a1))
def fm(r): 
#  dr = np.sqrt(r.dot(r)) - rmax/3.
#  return np.tanh(dr)
  if np.sqrt(r.dot(r))<rmax/3: return 1.0
  else: return -1.0
h.add_sublattice_imbalance(fm)
#h.add_haldane(lambda r1,r2: fm((r1+r2)/2))
topology.berry_green_map(h,k=[0.,0.,0.0],nrep=3,
        integral=True,eps=1e-4,delta=1e-2,operator="valley")
