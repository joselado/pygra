
import sys
import os

from pygra import geometry

g = geometry.honeycomb_lattice()
h = g.get_hamiltonian(has_spin=True)

h.get_bands(operator="valley")
