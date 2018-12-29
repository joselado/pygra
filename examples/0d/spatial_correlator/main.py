# Add the root path of the pygra library
import os ; import sys ; sys.path.append(os.environ['PYGRAROOT'])

import numpy as np
import matplotlib.pyplot as plt
import time
from pygra import geometry  # library to create crystal geometries
from pygra import hamiltonians  # library to work with hamiltonians
from pygra import sculpt  # to modify the geometry
from pygra import correlator
from pygra import kpm
g = geometry.chain()
g = g.supercell(10)
g.dimensionality = 0
h = g.get_hamiltonian(has_spin=False)
n = len(g.r)
h.shift_fermi(1.0)
cs = [correlator.gs_correlator(h.intra,i=0,j=i) for i in range(n)]
plt.plot(range(n),cs,marker="o")
plt.show()
