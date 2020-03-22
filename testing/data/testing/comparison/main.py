import geometry  # library to create crystal geometries
import hamiltonians  # library to work with hamiltonians
import input_tb90 as in90
import heterostructures
import sys
import sculpt  # to modify the geometry
import numpy as np
import klist


ns = np.arange(1,7,1)
t1s = []
t2s = []

for ncell in ns:
  
  g = geometry.honeycomb_lattice()  # create a honeycomb lattice
  
  h2 = g.get_hamiltonian() # create hamiltonian
  h2.remove_spin()
  ncell = int(ncell) 
#  ncell = 8
  g = g.supercell(ncell)
  h1 = g.get_hamiltonian() # create hamiltonian
  h1.remove_spin()
  
  
  
  
  import green
  
  delta = 0.02
  
  e = 0.7
  
  ez = e + 1j*delta # complex energy
  
  def renor_dos(e):
    g,selfe = green.bloch_selfenergy(h1,energy=e,delta=delta,nk=200,
                                       mode="renormalization")
    emat = np.matrix(np.identity(len(g)))*(e + delta*1j)  # E +i\delta 
    return g
  
  
  
  
  #g1 = renor_dos(e)  # compute kpoints in parallel
  #diag1 = [g1[i,i] for i in range(len(g1))]
  
  
  #g = g.supercell(nrep)
  import dyson2d
  import time
  t0 = time.perf_counter()
  # renormalization method
  g1 = renor_dos(e)  # compute kpoints in parallel
  t1 = time.perf_counter()
  # bloch method
  g2 = dyson2d.dyson2d(h2.intra,h2.tx,h2.ty,h2.txy,h2.txmy,ncell,ncell,300,ez) 
  t2 = time.perf_counter()
  print "Renorm = ",t1-t0,"      Bloch = ",t2-t1
  print "Error = ",np.max(np.abs(g1-g2)),np.max(np.abs(g1))
  t1s += [t1-t0]
  t2s += [t2-t1]


import pylab as py

py.plot(ns,t1s,marker="o")
py.plot(ns,t2s,marker="o")

py.show()

