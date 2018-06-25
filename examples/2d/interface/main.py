
import sys
sys.path.append("../../../pygra")  # add pygra library

import geometry
import topology
import klist

g = geometry.honeycomb_lattice()
h = g.get_hamiltonian(has_spin=True)
h1 = h.copy()
h2 = h.copy()
#h1.add_sublattice_imbalance(0.5)
h1.add_haldane(0.1)
#h2.add_sublattice_imbalance(-0.5)
h2.add_haldane(-0.1)

import kdos
kdos.interface(h1,h2)
