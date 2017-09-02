import geometry  # library to create crystal geometries
import hamiltonians  # library to work with hamiltonians
import input_tb90 as in90
import heterostructures
import sys
import sculpt  # to modify the geometry
import numpy as np
import klist

g = geometry.honeycomb_lattice()  # create a honeycomb lattice


h = g.get_hamiltonian() # create hamiltonian
h.remove_spin()

import green

delta = 0.02

e = 0.7

ez = e + 1j*delta # complex energy

def renor_dos(e):
  g,selfe = green.bloch_selfenergy(h,energy=e,delta=delta,nk=200,
                                     mode="renormalization")
  emat = np.matrix(np.identity(len(g)))*(e + delta*1j)  # E +i\delta 
  return g




#g1 = renor_dos(e)  # compute kpoints in parallel
#diag1 = [g1[i,i] for i in range(len(g1))]


#g = g.supercell(nrep)
import dyson2d
import time
dos2 = []
dos1 = []
es = np.linspace(-4.0,4.0,100)
for e in es: 
  t0 = time.clock()
  ez = e+delta*1j
  # renormalization method
  g1 = renor_dos(e)  # compute kpoints in parallel
  diag1 = [g1[i,i].imag for i in range(len(g1))]
  t1 = time.clock()
  
  # bloch method
  g2 = dyson2d.dyson2d(h.intra,h.tx,h.ty,h.txy,h.txmy,2,2,300,ez) 
  diag2 = [g2[i,i].imag for i in range(len(g2))]
  t2 = time.clock()
  print "Renorm = ",t1-t0,"      Bloch = ",t2-t1

  dos2 += [-sum(diag2)]
  dos1 += [-sum(diag1)]

import pylab as py
py.plot(es,dos1,c="red")
py.plot(es,dos2)

py.show()

