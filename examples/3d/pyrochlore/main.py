import sys
import numpy as np
import os
sys.path.append(os.environ["PYGRAROOT"])

from pygra import geometry
from pygra import sculpt

g = geometry.pyrochlore_lattice()
h = g.get_hamiltonian()
h.turn_dense()
g.center() # center the geometry
g.write()
ms = [-ri for ri in g.r] # magnetizations
h.get_bands()

