# Add the root path of the pygra library
import os ; import sys 
sys.path.append(os.path.dirname(os.path.realpath(__file__))+"/../../../src")




from pygra import geometry
g = geometry.honeycomb_lattice()
h = g.get_hamiltonian(has_spin=True) # create hamiltonian of the system
h = h + h
h.get_bands()






