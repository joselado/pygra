# Add the root path of the pygra library
import os ; import sys ; sys.path.append(os.environ['PYGRAROOT'])

# zigzag ribbon
from pygra importgeometry
import operators
g = geometry.honeycomb_zigzag_ribbon(10) # create geometry of a zigzag ribbon
h = g.get_hamiltonian() # create hamiltonian of the system
h.add_peierls(0.05)
import ldos
#ldos.multi_ldos(h,op=h.get_operator("sz"))
#h.get_bands(operator=h.get_operator("valley"))
#exit()
ldos.multi_ldos(h,op=h.get_operator("valley"))
