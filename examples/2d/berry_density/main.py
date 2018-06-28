
import sys
sys.path.append("../../../pygra")  # add pygra library

import geometry
import topology
import klist

g = geometry.honeycomb_lattice()
h = g.get_hamiltonian(has_spin=False)
h.add_haldane(0.1)
import dos
import topology
topology.berry_density(h)

#h.get_bands()
#dos.dos(h,nk=100,use_kpm=True)
