import sys
sys.path.append("../../../pygra")  # add pygra library

import geometry  # library to create crystal geometries
import hamiltonians  # library to work with hamiltonians
import sculpt  # to modify the geometry
import correlator
import numpy as np
import matplotlib.pyplot as plt
import kpm
import time

g = geometry.chain()
g = g.supercell(10)
g.dimensionality = 0
h = g.get_hamiltonian(has_spin=False)
n = len(g.r)
h.shift_fermi(1.0)
cs = [correlator.gs_correlator(h.intra,i=0,j=i) for i in range(n)]


plt.plot(range(n),cs,marker="o")
plt.show()

