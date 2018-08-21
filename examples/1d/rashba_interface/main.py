# zigzag ribbon
import sys
sys.path.append("../../../pygra")  # add pygra library

import geometry
g = geometry.honeycomb_zigzag_ribbon(10) # create geometry of a zigzag ribbon
h = g.get_hamiltonian(has_spin=True) # create hamiltonian of the system

def fr(r):
    if r[1]<0.0:  return 0.3
    else: return -0.3

h.add_rashba(fr)


h.get_bands() # calculate band structure
