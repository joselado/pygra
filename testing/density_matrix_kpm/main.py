import sys
sys.path.append("../../pygra")  # add pygra library

import geometry  # library to create crystal geometries
import hamiltonians  # library to work with hamiltonians
import sculpt  # to modify the geometry
import correlator
import numpy as np
import matplotlib.pyplot as plt
import kpm
import densitymatrix
import time

restart = True
#restart = True

if True:
  g = geometry.honeycomb_lattice()
  g = g.supercell(10)
  g.dimensionality = 0
  g.write()

else:
  g = geometry.read()

print("Generating Hamiltonian")
h = g.get_hamiltonian(is_sparse=True)


#h.get_bands()
#exit()

#h.remove_spin()

h.add_sublattice_imbalance(.3)

#h.shift_fermi(.5)

h.add_rashba(.5)
h.add_zeeman([0.,0.,0.2])

#h.intra += np.diag(np.random.random(h.intra.shape[0]))



def cij(i,j): # correlation between sites i,j
  pairs = [(2*i,2*j),(2*i+1,2*j),(2*i,2*j+1),(2*i+1,2*j+1)]
#  pairs = [(2*i,2*j),(2*i+1,2*j+1)]
  y1 = densitymatrix.restricted_dm(h,mode="KPM",pairs=pairs,npol=500)
#  y1 = densitymatrix.restricted_dm(h,mode="full",pairs=pairs,npol=500)
#  y1 = np.array(y1).reshape(2,2)
#  y1 = np.linalg.det(y1) # determinant
#  print(y1)
#  print(np.linalg.svd(y1,compute_uv=False))
#  y2 = np.linalg.svd(y1,compute_uv=False)
#  print(np.sum(y2),np.sum(y1))
  return np.sum(y1) # return correlation



i = sculpt.get_closest(g,n=1)[0] # get the central point
x = sculpt.get_closest(g,n=80,r0=g.r[i])
y1 = [cij(i,j) for j in x] # get the different correlations

# print in a file
fo1 = open("CORRELATION_MAP_REAL.OUT","w")
fo2 = open("CORRELATION_MAP_IMAG.OUT","w")

for ii in range(len(y1)):
  j = x[ii]
  fo1.write(str(g.x[j]-g.x[i])+"   ") # xposition
  fo2.write(str(g.x[j]-g.x[i])+"   ") # xposition
  fo1.write(str(g.y[j]-g.y[i])+"   ") # yposition
  fo2.write(str(g.y[j]-g.y[i])+"   ") # yposition
  fo1.write(str(y1[ii].real)+"\n") # xposition
  fo2.write(str(y1[ii].imag)+"\n") # xposition
  
fo1.close()
fo2.close()

exit()

print(y1-y2)

print("Time KPM = ",t2-t1)
print("Time in inversion = ",t3-t2)
#print(np.trapz(y,x=x,dx=x[1]-x[0]))

plt.subplot(1,2,1)
plt.plot(x,y1.real,marker="o",label="KPM")
plt.plot(x,y2.real,marker="o",label="Green")

plt.legend()

plt.subplot(1,2,2)
plt.plot(x,y1.imag,marker="o",label="KPM")
plt.plot(x,y2.imag,marker="o",label="Green")

plt.legend()

plt.show()
