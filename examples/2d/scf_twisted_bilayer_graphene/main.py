import os
import sys
import numpy as np
from pygra import geometry
from pygra import hamiltonians
from pygra import klist
from pygra import sculpt
from pygra import specialgeometry
from pygra import scftypes


g = specialgeometry.twisted_bilayer(11)
g.write()
from pygra import specialhopping
h = g.get_hamiltonian(is_sparse=True,has_spin=False,is_multicell=False,
     mgenerator=specialhopping.twisted_matrix(ti=0.3,lambi=7.0))
h.turn_dense()
def ff(r):
    return 0.2*r[2]
    
h.shift_fermi(ff)

mf = h.intra*0.0 +0.0j #scftypes.guess(h,mode="antiferro")
scf = scftypes.selfconsistency(h,nkp=1,filling=0.5+6./h.intra.shape[0],g=2.0,
                mix=0.9,mf=mf,mode="U")

scf.hamiltonian.get_bands()



