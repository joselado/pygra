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


g = specialgeometry.twisted_bilayer(6)
#g = geometry.honeycomb_lattice()
g.write()
#g = geometry.read()
#exit()
from specialhopping import twisted,twisted_matrix

h = g.get_hamiltonian(is_sparse=True,has_spin=False,is_multicell=False,
     mgenerator=twisted_matrix(ti=0.4,lambi=7.0))

import density

#d = density.density(h,window=0.1,e=0.025)
#h.shift_fermi(d)
h.get_bands(num_bands=20)
