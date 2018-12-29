# Add the root path of the pygra library
import os ; import sys ; sys.path.append(os.environ['PYGRAROOT'])

import numpy as np
from pygra import geometry
from pygra import ldos
g = geometry.honeycomb_zigzag_ribbon()
h = g.get_hamiltonian(has_spin=True)
ldos.multi_ldos(h,nk=4,es=np.linspace(-1,1,100),delta=0.1,nrep=3)
