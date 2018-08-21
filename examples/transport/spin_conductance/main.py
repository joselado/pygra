
import sys
sys.path.append("../../../pygra")  # add pygra library

import geometry
import heterostructures
import numpy as np
import matplotlib.pyplot as plt

g = geometry.honeycomb_zigzag_ribbon(5)

h = g.get_hamiltonian()
h.add_kane_mele(0.1)
#h.get_bands()
#exit()
h1 = h.copy() # copy
h2 = h.copy() # copy

ht = heterostructures.create_leads_and_central(h1,h2,h1) # create the junction
ht.delta = 1e-3 # imaginary part of the energy

es = np.linspace(-.5,.5,20) # grid of energies
ts = [ht.didv(e) for e in es] # calculate transmission

plt.plot(es,ts,marker="o")
plt.ylim([0,4.1])
plt.show()


