import os
import sys
sys.path.append(os.environ["PYGRAROOT"])
import geometry
import hamiltonians
import numpy as np
import klist
import sculpt

import specialgeometry


g = specialgeometry.twisted_bilayer(2)
g.write()
from specialhopping import twisted_matrix

h = g.get_hamiltonian(is_sparse=True,has_spin=False,is_multicell=False,
     mgenerator=twisted_matrix(ti=0.0,lambi=7.0))

h.turn_dense()
import density

import scftypes

mf = np.random.random(h.intra.shape) -.5
mf = np.matrix(mf)
mf = mf + mf.H

scf = scftypes.selfconsistency(h,nkp=5,filling=0.5,g=3.0,
              mix=0.9,mf=mf,mode="V")
h = scf.hamiltonian # get the Hamiltonian


import groundstate

groundstate.hopping(h,nrep=1,skip = lambda r1,r2: r1[2]*r2[2]<0) # write three replicas
h.get_bands() # calculate band structure
