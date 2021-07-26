# Add the root path of the pygra library
import os ; import sys 
sys.path.append(os.path.dirname(os.path.realpath(__file__))+"/../../../src")





from pygra import geometry
from pygra import topology
g = geometry.honeycomb_lattice()
h = g.get_hamiltonian()
h.add_kane_mele(0.022)
parity = topology.z2_invariant(h)
print("Z2 is ",parity)
h.get_bands()






