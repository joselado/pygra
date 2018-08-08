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
g = geometry.supercell2d(g,n1=4,n2=4)
h = hamiltonians.hamiltonian(g) # create hamiltonian
h.first_neighbors()  # create first neighbor hopping

#h.add_sublattice_imbalance(.1)
#h.remove_spin()

h.add_kane_mele(0.04)
h.remove_spin()
#h.add_rashba(.2)
#h.add_zeeman([0.,0.,.2])
es = np.linspace(-1.,1.,80)
#es = np.linspace(-.3,.3,80)
dos = []
dosv = []

vintra = h.intra.copy()
vintra[len(vintra)/2,len(vintra)/2] = 10000.
import time

for e in es:
  delta = 0.001
  print e
  g,selfe = green.bloch_selfenergy(h,energy=e,delta=delta,error=0.001,
                                     mode="adaptative")
  emat = np.matrix(np.identity(len(g)))*(e + delta*1j)
  gv = (emat - vintra -selfe).I   # Green function of a vacancy


  dos.append(-g.trace()[0,0].imag)
#  dosv.append(-gv.trace()[0,0].imag)
  dosv.append(-gv.trace()[0,0].imag)

#  dos.append(-green.bloch_selfenergy(h,energy=e,delta=0.1).imag)
py.plot(es,dos,marker="o")
py.plot(es,dosv,marker="o")
#print h.get_hk_gen()(.1)

h.write("hamiltonian.in")

py.show()

