
import sys
sys.path.append("../../../pygra")  # add pygra library

import geometry
import topology
import klist

g = geometry.honeycomb_lattice()
h = g.get_hamiltonian(has_spin=False)
h.add_sublattice_imbalance(0.5)
import dos
import topology
topology.berry_map(h,mode="Green")

#h.get_bands()
#dos.dos(h,nk=100,use_kpm=True)
