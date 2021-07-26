# Add the root path of the pygra library
import os ; import sys 
sys.path.append(os.path.dirname(os.path.realpath(__file__))+"/../../../src")





# zigzag ribbon
from pygra import geometry
g = geometry.honeycomb_zigzag_ribbon(10) # create geometry of a zigzag ribbon
h = g.get_hamiltonian(has_spin=False) # create hamiltonian of the system
h.add_antihaldane(0.1)
from pygra import ldos
ldos.spatial_energy_profile(h,operator=h.get_operator("current"),nk=100)







