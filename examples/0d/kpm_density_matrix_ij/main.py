# Add the root path of the pygra library
import os ; import sys ; sys.path.append(os.environ['PYGRAROOT'])

from pygra import geometry  # library to create crystal geometries
from pygra import hamiltonians  # library to work with hamiltonians
from pygra import sculpt  # to modify the geometry
from pygra import correlator
from pygra import kpm
from pygra import densitymatrix
import numpy as np
import matplotlib.pyplot as plt
import time
g = geometry.chain()
g = g.supercell(100)
g.dimensionality = 0
h = g.get_hamiltonian()
h.add_rashba(.5)
h.add_zeeman([0.,1.,0.])
h.intra += np.diag(np.random.random(h.intra.shape[0]))
i = 0
j = 9
t1 = time.perf_counter()
rand = lambda : np.random.randint(0,40)
pairs = [(i,i+np.random.randint(1,8)) for i in range(10,20)]
y = densitymatrix.restricted_dm(h,mode="KPM",pairs=pairs)
t2 = time.perf_counter()
y2 = densitymatrix.restricted_dm(h,mode="full",pairs=pairs)
t3 = time.perf_counter()
print("Time KPM mode = ",t2-t1)
print("Time in full mode = ",t3-t2)
#print(np.trapz(y,x=x,dx=x[1]-x[0]))
plt.subplot(1,2,1)
x = range(len(y))
plt.plot(x,y.real,marker="o",label="KPM")
plt.plot(x,y2.real,marker="o",label="Green")
plt.legend()
plt.subplot(1,2,2)
plt.plot(x,y.imag,marker="o",label="KPM")
plt.plot(x,y2.imag,marker="o",label="Green")
plt.legend()
plt.show()
