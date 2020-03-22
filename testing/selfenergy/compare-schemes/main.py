import geometry  # library to create crystal geometries
import hamiltonians  # library to work with hamiltonians
import input_tb90 as in90
import heterostructures
import sys
import sculpt  # to modify the geometry
import numpy as np
import klist
import pylab as py
import green

g = geometry.honeycomb_lattice()  # create a honeycomb lattice
#g = geometry.square_ribbon(1) 
g = geometry.supercell2d(g,n1=1,n2=1)
h = hamiltonians.hamiltonian(g) # create hamiltonian
h.first_neighbors()  # create first neighbor hopping

#h.add_sublattice_imbalance(.1)
h.remove_spin()

#h.add_kane_mele
#h.add_rashba(.2)
#h.add_zeeman([0.,0.,.2])
es = np.linspace(-1.,1.,21)
dos = []
dosv = []

vintra = h.intra.copy()
vintra[len(vintra)/2,len(vintra)/2] = 10000.
import time

for e in es:
  delta = 0.001
  told = time.perf_counter()  
#  g,selfe = green.bloch_selfenergy(h,energy=e,delta=delta,nk=500,
#                                     mode="renormalization")
#  print time.perf_counter() - told
  told = time.perf_counter()  
#  g2,selfe2 = green.bloch_selfenergy(h,energy=e,delta=delta,nk=200,
#                                     mode="full")
#  print time.perf_counter() - told
  told = time.perf_counter()  
  g3,selfe3 = green.bloch_selfenergy(h,energy=e,delta=delta,nk=500,
                                     mode="adaptive")
  g = g3
  selfe = selfe3
#  print time.perf_counter() - told
  told = time.perf_counter()  
#  print np.max(np.abs(g-g2)),np.max(np.abs(selfe-selfe2))
#  print np.max(np.abs(g2-g3)),np.max(np.abs(selfe2-selfe3))
  print np.max(np.abs(g-g3)),np.max(np.abs(selfe-selfe3))
  print
  emat = np.matrix(np.identity(len(g)))*(e + delta*1j)
  gv = (emat - vintra -selfe).I   # Green function of a vacancy
#  gv2 = (emat - vintra -selfe2).I   # Green function of a vacancy
  gv3 = (emat - vintra -selfe3).I   # Green function of a vacancy

  
#  print np.max(np.abs(gv-gv2))
#  print np.max(np.abs(gv2-gv3))
  print np.max(np.abs(gv3-gv))
  print


  dos.append(-g.trace()[0,0].imag)
#  dosv.append(-gv.trace()[0,0].imag)
  dosv.append(-gv.trace()[0,0].imag)

#  dos.append(-green.bloch_selfenergy(h,energy=e,delta=0.1).imag)
py.plot(es,dos,marker="o")
py.plot(es,dosv,marker="o")
#print h.get_hk_gen()(.1)


py.show()

