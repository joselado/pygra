# Add the root path of the pygra library
import os ; import sys 
sys.path.append(os.path.dirname(os.path.realpath(__file__))+"/../../../src")





from pygra import geometry
from pygra import topology
from pygra import klist
from pygra import kdos
g = geometry.diamond_lattice_minimal()
h = g.get_hamiltonian(has_spin=True)
h.intra *= 1.3
h.add_kane_mele(0.05)
kdos.surface(h,operator=None)






