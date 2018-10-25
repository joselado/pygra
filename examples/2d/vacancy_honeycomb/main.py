
import sys
sys.path.append("../../../pygra")  # add pygra library

import geometry
import topology
import klist

g = geometry.honeycomb_lattice()
g = g.supercell(2)
g = g.remove(0)
h = g.get_hamiltonian(has_spin=True)
import dos
import operators
f = operators.get_inplane_valley(h)
h.get_bands(operator=f)
#dos.dos(h,nk=100,use_kpm=True)
