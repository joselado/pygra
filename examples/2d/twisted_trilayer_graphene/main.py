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


g = specialgeometry.twisted_multilayer(6,rot=[0,1,0])
#g = g.supercell(2)
#g = geometry.honeycomb_lattice()
g.write()
#g = geometry.read()
#exit()
from specialhopping import twisted_matrix

h = g.get_hamiltonian(is_sparse=True,has_spin=False,is_multicell=False,
     mgenerator=twisted_matrix(ti=0.4,lambi=7.0))

import density

#def ff(r): return 0.05*r[2]
#h.shift_fermi(ff) # shift chemical potential
#h.set_filling(nk=4,extrae=0.) # set to half filling + 2 e
#d = density.density(h,window=0.1,e=0.025)
#h.shift_fermi(d)
#h.turn_sparse()
#h.turn_dense()
h.get_bands(num_bands=40)
