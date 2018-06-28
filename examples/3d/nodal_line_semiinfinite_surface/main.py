
import sys
sys.path.append("../../../pygra")  # add pygra library

import geometry
import topology
import klist

g = geometry.diamond_lattice_minimal()
h = g.get_hamiltonian(has_spin=True)
#h.intra *= 0.8
h.add_kane_mele(0.01)
hs = h.copy()
#hs.add_magnetism([[0.,0.,-0.1],[0.,0.,0.2]])
import kdos
kdos.surface(h,hs=hs.intra,operator=h.get_operator("sz"))
