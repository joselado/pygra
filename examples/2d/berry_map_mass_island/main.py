import os
import sys
sys.path.append("../../../pygra")
#sys.path.append(os.environ["QHROOT"]+"/pysrc")
import geometry
import hamiltonians
import numpy as np
import klist
import sculpt

import specialgeometry

#raise # this does not work yet

g = geometry.honeycomb_lattice()

g = g.supercell(11)
h = g.get_hamiltonian(has_spin=False)



def fm(r): 
#  r = r -np.array([0.,3.0,0.])
  if r.dot(r)<7.0: return 0.3
  else: return -0.3

h.add_sublattice_imbalance(fm)

import topology
topology.berry_green_map(h,k=[0.3333333,0.3333333,0.0],nrep=3,integral=True)
