# Add the root path of the pygra library
import os ; import sys ; sys.path.append(os.environ['PYGRAROOT'])

# zigzag ribbon
from pygra importgeometry
import ribbon
g = geometry.honeycomb_lattice()
g = ribbon.bulk2ribbon(g,n=5,boundary=[6,1])
h = g.get_hamiltonian(has_spin=False)
h.get_bands()
g = g.supercell(4)
g.write()
