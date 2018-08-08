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
import topology

g = geometry.honeycomb_lattice()  # create a honeycomb lattice
h = g.get_hamiltonian() # create the hamiltonian
h.add_sublattice_imbalance(.1)
#h.add_rashba(.01)
#h.add_zeeman([0.,0.,.2])
h.add_kane_mele(0.1)
#h.remove_spin()
kl = klist.default(h,100)
#be = [topology.berry_curvature(h,k) for k in kl]
print topology.z2_invariant(h,nk=100)
#print topology.chern(h,nk=50)

#py.plot(kl,be)
#py.show()
