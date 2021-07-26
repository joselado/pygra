# Add the root path of the pygra library
import os ; import sys 
sys.path.append(os.path.dirname(os.path.realpath(__file__))+"/../../../src")





from pygra import geometry
from pygra import topology
from pygra import dos
g = geometry.honeycomb_lattice()
h = g.get_hamiltonian(has_spin=True)
h.get_bands(operator="velocity")






