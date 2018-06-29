
import sys
sys.path.append("../../../pygra")  # add pygra library

import geometry
import topology
import klist

g = geometry.honeycomb_lattice()
h = g.get_hamiltonian(has_spin=False)
h.add_sublattice_imbalance(0.05)
import dos
import topology
op = h.get_operator("valley",projector=True) # valley operator
op = None
topology.write_berry(h,mode="Green",operator=op)

#h.get_bands()
#dos.dos(h,nk=100,use_kpm=True)
