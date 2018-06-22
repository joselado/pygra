# zigzag ribbon
import sys
sys.path.append("../../../pygra")  # add pygra library

import geometry
g = geometry.honeycomb_armchair_ribbon(60) # create geometry of a zigzag ribbon
h = g.get_hamiltonian(has_spin=True) # create hamiltonian of the system
h.add_haldane(.1) # add Haldane coupling
h.get_bands() # calculate band structure
#h.get_bands(operator=h.get_operator("valley"))
