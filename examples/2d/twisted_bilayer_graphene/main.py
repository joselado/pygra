# Add the root path of the pygra library
import os ; import sys ; sys.path.append(os.environ['PYGRAROOT'])

from pygra import geometry
from pygra import hamiltonians
import numpy as np
from pygra import klist
from pygra import sculpt
from pygra import specialgeometry
from pygra import parallel
parallel.cores = 7


g = specialgeometry.twisted_bilayer(7)
#g = g.supercell(3)
#g = geometry.honeycomb_lattice()
from pygra.specialhopping import twisted_matrix
h = g.get_hamiltonian(is_sparse=True,has_spin=False,is_multicell=False,
     mgenerator=twisted_matrix(ti=0.4,lambi=7.0))
#h.set_filling(nk=3,extrae=1.) # set to half filling + 2 e
#d = density.density(h,window=0.1,e=0.025)
#h.shift_fermi(d)
#h.turn_sparse()
from pygra import algebra
algebra.accelerate = False
h.get_bands(nk=100)
