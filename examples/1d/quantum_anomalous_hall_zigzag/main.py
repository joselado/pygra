# Add the root path of the pygra library
import os ; import sys ; sys.path.append(os.environ['PYGRAROOT'])

# zigzag ribbon
from pygra import geometry
g = geometry.honeycomb_zigzag_ribbon(10) # create geometry of a zigzag ribbon
h = g.get_hamiltonian() # create hamiltonian of the system
h.add_rashba(0.2) # add Rashba spin orbit coupling
h.add_zeeman([0.,0.,0.2]) # add off-plane Zeeman coupling
h.get_bands(nk=300) # calculate band structure
