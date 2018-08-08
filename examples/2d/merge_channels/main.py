
import sys
sys.path.append("../../../pygra")  # add pygra library

import geometry
import topology
import klist

g = geometry.honeycomb_lattice()
h = g.get_hamiltonian(has_spin=False)
h1 = h.copy()
h2 = h.copy()
h1.add_sublattice_imbalance(0.5)
h2.add_sublattice_imbalance(-0.2)
import merge
h = merge.merge_channels(h1,h2) # merge spin up and down channels
h.get_bands(operator="sz")
#dos.dos(h,nk=100,use_kpm=True)
