# zigzag ribbon
import sys
import os
sys.path.append(os.environ["PYGRAROOT"])  # add pygra library

from pygra import geometry
g = geometry.honeycomb_zigzag_ribbon(5) # create geometry of a zigzag ribbon
h = g.get_hamiltonian() # create hamiltonian of the system
h.get_bands()
