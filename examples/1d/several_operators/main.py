# Add the root path of the pygra library
import os ; import sys ; sys.path.append(os.environ['PYGRAROOT'])

# zigzag ribbon
from pygra import geometry
g = geometry.honeycomb_zigzag_ribbon(10) # create geometry of a zigzag ribbon
h = g.get_hamiltonian(has_spin=False) # create hamiltonian of the system
h.add_peierls(0.05) # add magnetic field
op1 = h.get_operator("yposition") # position operator
op2 = h.get_operator("valley") # valley operator
h.get_bands(operator=[op1,op2]) # compute both expectation values
