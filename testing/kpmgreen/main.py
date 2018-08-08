import sys
sys.path.append("../../pygra")  # add pygra library

import geometry  # library to create crystal geometries
import hamiltonians  # library to work with hamiltonians
import sculpt  # to modify the geometry
import correlator
import numpy as np
import matplotlib.pyplot as plt
import kpm

g = geometry.chain()
g = g.supercell(100)
g.dimensionality = 0
h = g.get_hamiltonian()
h.shift_fermi(.4)

h.add_zeeman([.8,.8,.8])
h.add_rashba(.8)



i = 0
j = 7

(x,y,yi) = kpm.correlator0d(h.intra,npol=300,i=i,j=j)
(x2,y2,yi2) = correlator.correlator0d(h.intra,i=i,j=j,delta=0.1)
#print(np.trapz(y,x=x,dx=x[1]-x[0]))

plt.subplot(1,2,1)
plt.plot(x,y,marker="o",label="KPM")
plt.plot(x2,y2,marker="o",label="Green")

plt.legend()

plt.subplot(1,2,2)
plt.plot(x,yi,marker="o",label="KPM")
plt.plot(x2,yi2,marker="o",label="Green")

plt.legend()

plt.show()
