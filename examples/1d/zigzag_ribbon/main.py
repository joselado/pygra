# zigzag ribbon
import sys
sys.path.append("../../../pygra")  # add pygra library

import geometry
import operators
g = geometry.honeycomb_zigzag_ribbon(5) # create geometry of a zigzag ribbon
h = g.get_hamiltonian() # create hamiltonian of the system
import density
d = density.density(h,window=0.1,e=0.0)
#h.shift_fermi(d)
h.get_bands()
h.get_dos()
#h.add_zeeman([.0,.0,.2])
#h.get_bands(operator=operators.get_sz(h)) # calculate band structure
