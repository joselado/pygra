# Add the root path of the pygra library
import os ; import sys 
sys.path.append(os.path.dirname(os.path.realpath(__file__))+"/../../../src")





from pygra import geometry
from pygra import hamiltonians
from pygra import sculpt  # to modify the geometry
from pygra import correlator
from pygra import kpm
import numpy as np
import matplotlib.pyplot as plt
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
from pygra import ldos
#ldos.multi_ldos(h,np.linspace(-3.0,3.0,40),delta=0.1)
h.get_bands()






