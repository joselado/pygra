
import sys
sys.path.append("../../../pygra")  # add pygra library

# Compute the Gap of a honeycomb lattice as a function of the sublattice
# imbalance

import geometry
import gap
import numpy as np

ms = np.linspace(0.,0.3,30)
gs = [] # storage for the gaps
for m in ms:
  g = geometry.honeycomb_lattice()
  h = g.get_hamiltonian(has_spin=True)
  h.add_sublattice_imbalance(m)
  gg = gap.indirect_gap(h)
  gs.append(gg) # append gap
  print(m,gg,gg/m)



import matplotlib.pyplot as plt
plt.plot(ms,gs)
plt.xlabel("mass")
plt.ylabel("gap")
plt.show()

