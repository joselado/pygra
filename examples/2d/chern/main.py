
import sys
sys.path.append("../../../pygra")  # add pygra library

import geometry
import topology
import klist

g = geometry.honeycomb_lattice()
h = g.get_hamiltonian(has_spin=False)
h.add_haldane(0.05)
import dos
import topology
c = topology.chern(h)
print(c)
#dos.dos(h,nk=100,use_kpm=True)
