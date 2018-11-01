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


g = specialgeometry.twisted_bilayer(7)
#g = geometry.honeycomb_lattice()
g.write()
#g = geometry.read()
from specialhopping import twisted_matrix


h = g.get_hamiltonian(is_sparse=True,has_spin=False,is_multicell=False,
     mgenerator=twisted_matrix(ti=0.6,lambi=7.0))

import density

h.turn_dense()
#h.set_filling(nk=3,extrae=1.) # set to half filling + 2 e
#d = density.density(h,window=0.1,e=0.025)
def ff(r):
    return 0.2*r[2]
    
h.shift_fermi(ff)

import scftypes
mf = h.intra*0.0 +0.0j #scftypes.guess(h,mode="antiferro")
scf = scftypes.selfconsistency(h,nkp=1,filling=0.5+6./h.intra.shape[0],g=0.0,
                mix=0.9,mf=mf,mode="U")

scf.hamiltonian.get_bands()



