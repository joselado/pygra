# zigzag ribbon
import sys
sys.path.append("../../../pygra")  # add pygra library

import geometry
g = geometry.honeycomb_armchair_ribbon(10) # create geometry of a zigzag ribbon
h = g.get_hamiltonian() # create hamiltonian of the system
h.remove_spin() # remove spin degree of freedom
h.get_bands() # calculate band structure
