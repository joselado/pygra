# Add the root path of the pygra library
import os ; import sys ; sys.path.append(os.environ['PYGRAROOT'])

from pygra import geometry
from pygra import topology
from pygra import dos
g = geometry.honeycomb_lattice()
h = g.get_hamiltonian(has_spin=True)
h.set_filling(0.75)
h.get_bands()
