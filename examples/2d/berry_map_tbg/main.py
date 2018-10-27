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

g = specialgeometry.twisted_bilayer(9)
from specialhopping import twisted_matrix

h = g.get_hamiltonian(is_sparse=True,has_spin=False,is_multicell=False,
     mgenerator=twisted_matrix(ti=0.4,lambi=7.0))

h.turn_dense()



def ff(r): return r[2]*0.05

h.shift_fermi(ff) # interlayer bias
h.set_filling(nk=3,extrae=0.) # set to half filling + 2 e
#h.shift_fermi(-0.08)
#h.turn_sparse()
#h.get_bands(num_bands=20)
#exit()
import topology
topology.berry_green_map(h,k=[-0.333333,0.33333,0.0],nrep=3,integral=False)
#topology.berry_green_map(h,k=[0.5,0.0,0.0],nrep=3,integral=False)
#topology.berry_green_map(h,k=[0.0,-0.0,0.0],nrep=3,integral=False)
h.get_bands()
