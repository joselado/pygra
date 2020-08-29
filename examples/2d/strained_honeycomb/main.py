# Add the root path of the pygra library
import os ; import sys ; sys.path.append(os.environ['PYGRAROOT'])

from pygra import geometry
from pygra import topology
from pygra import specialhopping
from pygra import dos
g = geometry.honeycomb_lattice()
g = geometry.triangular_lattice()
g = g.supercell(3)
mgen = specialhopping.strained_hopping_matrix(g,dt=0.2,k=2)
h = g.get_hamiltonian(has_spin=False,mgenerator=mgen)
h.write_hopping()
h.get_bands()
