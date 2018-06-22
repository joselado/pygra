
import sys
sys.path.append("../../../pygra")  # add pygra library

import geometry
import topology
import klist

g = geometry.honeycomb_lattice()
h = g.get_hamiltonian()

h.add_kane_mele(0.022)
#h.add_sublattice_imbalance(0.2)


parity = topology.z2_invariant(h)
print("Z2 is ",parity)

h.get_bands(kpath=klist.default(g))
