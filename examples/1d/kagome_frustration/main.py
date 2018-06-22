import sys
import numpy as np
import os
sys.path.append("../../pygra")

import geometry
import sculpt

g = geometry.kagome_lattice()
#g = geometry.honeycomb_lattice()
g.has_sublattice = True
g.sublattice = [-1,1,0]
import ribbon

g = ribbon.bulk2ribbon(g,n=20)
h = g.get_hamiltonian()
ms = [] # zeeman fields
m1 = np.array([1.,0.,0.])
m2 = np.array([-.5,np.sqrt(3.)/2.,0.])
m3 = np.array([-.5,-np.sqrt(3.)/2.,0.])
mm = 3.0
for (r,s) in zip(g.r,g.sublattice):
  if r[1]<0.0:
    if s==-1: ms.append(m1*mm)
    if s==1: ms.append(m2*mm)
    if s==0: ms.append(m3*mm)
  else: ms.append([0.,0.,0.])

# swave
def fs(r):
  if r[1]>0.0: return 0.3
  else: return 0.0
h.add_magnetism(ms)
h.add_swave(fs)
h.shift_fermi(fs)
h.get_bands(operator="interface")
exit()
maf = []
#for s in g.sublattice:
#  if s==-1:
h.add_antiferromagnetism(0.5)
h = h.get_bands()

