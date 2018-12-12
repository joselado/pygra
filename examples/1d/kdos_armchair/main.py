# zigzag ribbon
import sys

from pygra import geometry
g = geometry.honeycomb_armchair_ribbon(100) # create geometry of a zigzag ribbon
h = g.get_hamiltonian(has_spin=False) # create hamiltonian of the system

from pygra import kdos
kdos.kdos_bands(h)
