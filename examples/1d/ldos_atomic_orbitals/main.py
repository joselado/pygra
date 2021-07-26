# Add the root path of the pygra library
import os ; import sys 
sys.path.append(os.path.dirname(os.path.realpath(__file__))+"/../../../src")





# zigzag ribbon
from pygra import geometry
g = geometry.honeycomb_armchair_ribbon(2) # create geometry of a zigzag ribbon
g = geometry.chain(30) # create geometry of a zigzag ribbon
g.dimensionality = 0
g.write()
h = g.get_hamiltonian()
from pygra import ldos
ldos.multi_ldos(h,projection="atomic")






