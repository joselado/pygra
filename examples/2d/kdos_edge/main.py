# Add the root path of the pygra library
import os ; import sys 
sys.path.append(os.path.dirname(os.path.realpath(__file__))+"/../../../src")




from pygra import geometry
from pygra import kdos
g = geometry.honeycomb_lattice()
h = g.get_hamiltonian()
h.add_haldane(0.05)
kdos.surface(h)







