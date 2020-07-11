# Add the root path of the pygra library
import os ; import sys ; sys.path.append(os.environ['PYGRAROOT'])

from pygra import geometry
from pygra import meanfield
import numpy as np


omega = 1./np.sqrt(2)

g = geometry.bichain()
g = g.supercell(20) # get the geometry
g.dimensionality = 0

h = g.get_hamiltonian() # compute Hamiltonian
delta = .0
maf = .5
def fsc(r): return delta*np.cos(omega*np.pi*2*r[0])
def faf(r): return maf*np.sin(omega*np.pi*2*r[0])
h.add_antiferromagnetism(faf)
h.add_swave(fsc)

mf = meanfield.guess(h,"random")

mf = None

scf = meanfield.Vinteraction(h,V1=1.0,mf=mf,
        filling=0.5,mix=0.1,
        compute_normal=True,
        compute_dd=False,
        compute_anomalous=True)


hscf = scf.hamiltonian


(inds,es) = h.get_bands()
(indsscf,esscf) = hscf.get_bands()


import matplotlib.pyplot as plt

plt.scatter(range(len(es)),es,c="red",label="Non-interacting")
plt.scatter(range(len(esscf)),esscf,c="blue",label="Interacting")

plt.legend()

plt.show()



