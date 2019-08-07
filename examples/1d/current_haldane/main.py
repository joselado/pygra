# Add the root path of the pygra library
import os ; import sys ; sys.path.append(os.environ['PYGRAROOT'])

# zigzag ribbon
from pygra import geometry
g = geometry.honeycomb_armchair_ribbon(20) # create geometry of a zigzag ribbon
h = g.get_hamiltonian(has_spin=False) # create hamiltonian of the system
h.add_haldane(0.05)
#exit()
from pygra import ldos
ldos.spatial_energy_profile(h,operator=h.get_operator("current"),nk=100)

