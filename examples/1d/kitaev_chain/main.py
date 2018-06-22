# zigzag ribbon
import sys
sys.path.append("../../../pygra")  # add pygra library

import numpy as np
import geometry
g = geometry.chain()
g = g.supercell(5)
#g = geometry.honeycomb_lattice()
g.write()
#g.dimensionality = 0
h = g.get_hamiltonian() # create hamiltonian of the system
h = h.get_multicell()
h.add_pwave(0.5)
import dos

dos.dos1d(h)
