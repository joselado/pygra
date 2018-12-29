# Add the root path of the pygra library
import os ; import sys ; sys.path.append(os.environ['PYGRAROOT'])

# zigzag ribbon
import numpy as np
from pygra import geometry
g = geometry.chain()
g = g.supercell(5)
#g = geometry.honeycomb_lattice()
g.write()
#g.dimensionality = 0
h = g.get_hamiltonian() # create hamiltonian of the system
h = h.get_multicell()
h.add_pwave(0.5)
from pygra import dos
dos.dos1d(h)
