import sys
import numpy as np
import os
sys.path.append(os.environ["PYGRAROOT"])

import geometry
import sculpt

g = geometry.pyrochlore_lattice()
h = g.get_hamiltonian()
h.turn_dense()
g.center() # center the geometry
g.write()
ms = [-ri for ri in g.r] # magnetizations
#h.add_magnetism(ms)
import dos
#dos.dos3d(h)
h.get_bands()
#g = g.supercell(3)


