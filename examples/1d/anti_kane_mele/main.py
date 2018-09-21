# zigzag ribbon
import sys
sys.path.append("../../../pygra")  # add pygra library

import geometry
g = geometry.honeycomb_zigzag_ribbon(10) # create geometry of a zigzag ribbon
h = g.get_hamiltonian() # create hamiltonian of the system
h.add_anti_kane_mele(.1) # add Kane mele spin orbit coupling
h.get_bands(operator="sz") # calculate band structure
