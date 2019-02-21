# Add the root path of the pygra library
import os ; import sys ; sys.path.append(os.environ['PYGRAROOT'])

from pygra import islands
from pygra import geometry
from pygra import spectrum
from pygra import operators

import numpy as np
g = islands.get_geometry(name="honeycomb",n=1.5,nedges=6,rot=0.0) # get an island
g = geometry.chain()
g = g.supercell(6)
#g.write()

h = g.get_hamiltonian(has_spin=False)
print("Operators")
m = h.get_hk_gen()([0.,0.,0.])
print(m)

from pygra import symmetry
symmetry.commuting_matrices(m)

