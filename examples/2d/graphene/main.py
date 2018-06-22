
import sys
sys.path.append("../../../pygra")  # add pygra library

import geometry
import topology
import klist

g = geometry.honeycomb_lattice()
h = g.get_hamiltonian(has_spin=True)
h.shift_fermi(g.z+2.)
import dos

h.get_bands()
#dos.dos(h,nk=100,use_kpm=True)
