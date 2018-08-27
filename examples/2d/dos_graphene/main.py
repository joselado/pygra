
import sys
sys.path.append("../../../pygra")  # add pygra library

import geometry
import topology
import klist

g = geometry.honeycomb_lattice()
h = g.get_hamiltonian(has_spin=False)
import dos
dos.dos(h,mode="ED",delta=0.01)
#dos.dos(h,nk=100,use_kpm=True)
