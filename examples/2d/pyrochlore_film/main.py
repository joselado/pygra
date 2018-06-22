import sys
import numpy as np
import os
sys.path.append(os.environ["PYGRAROOT"])

import geometry
import sculpt

g = geometry.pyrochlore_lattice()
#g = geometry.kagome_lattice()
import films
g = films.geometry_film(g,nz=10)
import ribbon
#g = ribbon.bulk2ribbon(g)
h = g.get_hamiltonian()
h.add_kane_mele(0.1)
h.turn_dense()
#g.center() # center the geometry
#g.write()
#ms = [-ri for ri in g.r] # magnetizations
#h.add_magnetism(ms)
import dos
#dos.dos3d(h)
h.get_bands(operator="zposition")
#g = g.supercell(3)


