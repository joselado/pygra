import os
import sys
sys.path.append(os.environ["PYGRAROOT"])
import geometry
import hamiltonians
import numpy as np
import klist
import sculpt

import specialgeometry


g = specialgeometry.twisted_bilayer(5)
g.write()
from specialhopping import twisted_matrix

h = g.get_hamiltonian(is_sparse=True,has_spin=False,is_multicell=False,
     mgenerator=twisted_matrix(ti=0.3,lambi=7.0))

h.add_haldane(0.1)
h.shift_fermi(-0.44)

import density

#h.set_filling(nk=3,extrae=1.) # set to half filling + 2 e
#d = density.density(h,window=0.1,e=0.025)
#h.shift_fermi(d)
#h.turn_sparse()
#h.get_bands(num_bands=20)
import topology
h.turn_dense()
#topology.write_berry(h)
topology.mesh_chern(h)
