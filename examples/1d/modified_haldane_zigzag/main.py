# Add the root path of the pygra library
import os ; import sys ; sys.path.append(os.environ['PYGRAROOT'])

# zigzag ribbon
from pygra import geometry
g = geometry.honeycomb_zigzag_ribbon(30) # create geometry of a zigzag ribbon
h = g.get_hamiltonian(has_spin=False) # create hamiltonian of the system
h.add_modified_haldane(.1) # add modified Haldane coupling
h.get_bands() # calculate band structure
