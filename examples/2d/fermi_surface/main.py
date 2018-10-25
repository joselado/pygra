
import sys
sys.path.append("../../../pygra")  # add pygra library

import geometry
import topology
import klist

g = geometry.triangular_lattice()
h = g.get_hamiltonian(has_spin=True)
#h.set_filling(nk=20)
h.get_bands()
