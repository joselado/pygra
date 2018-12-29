# Add the root path of the pygra library
import os ; import sys ; sys.path.append(os.environ['PYGRAROOT'])

# zigzag ribbon
from pygra import geometry
g = geometry.honeycomb_zigzag_ribbon(5) # create geometry of a zigzag ribbon
h = g.get_hamiltonian() # create hamiltonian of the system
h.get_bands()
