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

g = geometry.bichain()
g = g.supercell(40)
g.center()
g.dimensionality = 0
g.write()

def fs(r):
    if r[0]<0.0: return 0.5
    else: return 0.0

def faf(r):
    if r[0]>0.0: return 0.5
    else: return 0.0

h = g.get_hamiltonian()
h.add_antiferromagnetism(faf)
h.add_swave(fs)

import ldos
#ldos.multi_ldos(h,np.linspace(-3.0,3.0,40),delta=0.1)
h.get_bands()
