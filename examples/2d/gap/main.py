
import sys
sys.path.append("../../../pygra")  # add pygra library

import geometry
import gap
import numpy as np

ms = np.linspace(0.,0.3,30)
for m in ms:
  g = geometry.honeycomb_lattice()
  h = g.get_hamiltonian(has_spin=True)
  h.add_sublattice_imbalance(m)
  gg = gap.indirect_gap(h)
  print(m,gg,gg/m)
