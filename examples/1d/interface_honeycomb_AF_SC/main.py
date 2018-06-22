# zigzag ribbon
import sys
sys.path.append("../../../pygra")  # add pygra library

import geometry
import hybrid


# This script creates an interface between honeycomb AF and SC,
# showing a set of gap-less interface states


g = geometry.honeycomb_zigzag_ribbon(20) # create geometry of a zigzag ribbon
#g = geometry.honeycomb_armchair_ribbon(20) # create geometry of a zigzag ribbon
#g = geometry.bisquare_ribbon(20) # create geometry of a square ribbon
h = g.get_hamiltonian() # create hamiltonian of the system

#h.add_rashba(.05)

h1 = h.copy() # copy Hamiltonian
h2 = h.copy() # copy Hamiltonian

h1.add_antiferromagnetism(0.2) # add antiferromagnetism


h1.add_swave(0.0) # add electron-hole

h2.shift_fermi(.4) # dope the system
h2.add_swave(0.3) # add swave paring

h = hybrid.half_and_half(h1,h2,tlen=2) # create a ribbon with half h1 and half h2

h.get_bands() # calculate band structure
