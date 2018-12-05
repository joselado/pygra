
import sys
import os
sys.path.append(os.environ["PYGRAROOT"])  # add pygra library

from pygra import geometry

g = geometry.honeycomb_lattice()
h = g.get_hamiltonian(has_spin=True)

h.get_bands(operator="valley")
