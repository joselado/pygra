# zigzag ribbon
import sys
sys.path.append("../../../pygra")  # add pygra library

import geometry
import operators
g = geometry.honeycomb_zigzag_ribbon(5) # create geometry of a zigzag ribbon
h = g.get_hamiltonian() # create hamiltonian of the system
h.add_zeeman([.0,.0,.2])
h.get_bands(operator=operators.get_sz(h)) # calculate band structure
