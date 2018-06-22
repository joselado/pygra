import os
import sys
sys.path.append("../../../pygra")
import geometry
import hamiltonians
import numpy as np
import klist
import sculpt

import specialgeometry


g = specialgeometry.twisted_bilayer(20)
#g = geometry.honeycomb_lattice()
g.write()
#g = geometry.read()

from specialhopping import twisted,twisted_matrix

h = g.get_hamiltonian(is_sparse=True,has_spin=False,is_multicell=False,
     mgenerator=twisted_matrix(ti=0.4,lambi=7.0))

import kdos
kdos.kdos_bands(h,ntries=1)

#h.get_bands()
