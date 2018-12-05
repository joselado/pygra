
import sys
import os
sys.path.append(os.environ["PYGRAROOT"])  # add pygra library

from pygra import geometry
from pygra import topology

g = geometry.honeycomb_lattice()
h = g.get_hamiltonian(has_spin=True)
from pygra import kdos
kdos.surface(h)
