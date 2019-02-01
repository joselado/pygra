# Add the root path of the pygra library
import os ; import sys ; sys.path.append(os.environ['PYGRAROOT'])

from pygra import geometry
from pygra import specialhopping
import numpy as np
g = geometry.triangular_lattice()
fun = specialhopping.phase_C3(g,phi=0.3)
h = g.get_hamiltonian(has_spin=False,fun=fun)
h.turn_spinful(enforce_tr=True)
h.turn_dense()
h.get_bands(operator="sz")
