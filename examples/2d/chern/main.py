# Add the root path of the pygra library
import os ; import sys 
sys.path.append(os.path.dirname(os.path.realpath(__file__))+"/../../../src")




from pygra import geometry
from pygra import topology
g = geometry.honeycomb_lattice()
g = g.supercell(2)
h = g.get_hamiltonian()
h.add_rashba(0.3) # Rashba spin-orbit coupling
h.add_zeeman([0.,0.,0.3]) # Exchange field
c = topology.chern(h)
print("Chern number is ",c)







