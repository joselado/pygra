import geometry  # library to create crystal geometries
import hamiltonians  # library to work with hamiltonians
import sculpt  # to modify the geometry
import numpy as np
import pylab as py



g = geometry.honeycomb_lattice()  # create a honeycomb lattice
#g = geometry.square_lattice()  # create a honeycomb lattice
#g = geometry.kagome_lattice()  # create a honeycomb lattice
g = g.supercell(50) # create supercell
g.set_finite()


# create a hexagonal island


def f(x,y):
  """ Retain a plane"""
  return x>-3*(np.cos(np.pi/3)+1.)

#g = sculpt.rotate(g,np.pi/3.)

nedges = 3

for j in range(1):
  for i in range(nedges): # loop over rotations
    g = sculpt.intersec(g,f) # retain certain atoms
    g = sculpt.rotate(g,2.*np.pi/nedges)
  g.center()

g = sculpt.remove_unibonded(g)

h = g.get_hamiltonian()

hamiltonians.ldos(h,e=0.0)

g.write()
