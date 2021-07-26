# Add the root path of the pygra library
import os ; import sys 
sys.path.append(os.path.dirname(os.path.realpath(__file__))+"/../../../src")





from pygra import geometry
g = geometry.honeycomb_lattice()
g = g.supercell(4)
h = g.get_hamiltonian(has_spin=True)
from pygra import operators

op = h.get_operator("valley")
h.get_bands(operator=op)






