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
#  h2.add_rashba(0.1)
#  h2.remove_spin()
  ncell = int(ncell) 
#  ncell = 8
  g = g.supercell(ncell)
  h1 = g.get_hamiltonian() # create hamiltonian
#  h1.add_rashba(0.1)
#  h1.remove_spin()
  
  
  
  
  import green
  
  delta = 0.02
  
  e = 0.7
  
  ez = e + 1j*delta # complex energy
  
  def renor_dos(e):
    g,selfe = green.bloch_selfenergy(h1,energy=e,delta=delta,nk=200,
                                       mode="adaptative")
    emat = np.matrix(np.identity(len(g)))*(e + delta*1j)  # E +i\delta 
    return g,selfe
  
  
  
  
  #g1 = renor_dos(e)  # compute kpoints in parallel
  #diag1 = [g1[i,i] for i in range(len(g1))]
  
  
  #g = g.supercell(nrep)
  import time
  t0 = time.perf_counter()
  # renormalization method
  g1,selfe1 = renor_dos(e)  # compute kpoints in parallel
  t1 = time.perf_counter()
  # bloch method
  g2,selfe2,ins = green.supercell_selfenergy(h2,e=e,delta=delta,nk=300,nsuper=ncell)
  t2 = time.perf_counter()
  print "Error in intracell = ",np.max(np.abs(ins-h1.intra))
  print "Renorm = ",t1-t0,"      Bloch = ",t2-t1
  print "Error in bulk green = ",np.max(np.abs(g1-g2))
  print "Error in selfenergy = ",np.max(np.abs(selfe1-selfe2))
  t1s += [t1-t0]
  t2s += [t2-t1]


import pylab as py

py.plot(ns,t1s,marker="o")
py.plot(ns,t2s,marker="o")

py.show()

