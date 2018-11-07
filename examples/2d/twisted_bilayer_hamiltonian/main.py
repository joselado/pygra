import os
import sys
sys.path.append(os.environ["PYGRAROOT"]) # Path with libraries
import numpy as np
import specialgeometry

n = 7 # this is a parameter that controls the size of the moire unit cell
g = specialgeometry.twisted_bilayer(n) # get the geometry of the system
# g.r is the list with the positions in the unit cell
# g.a1 is the first lattice vector
# g.a2 is the second lattice vector


# This function will create hoppings in the structure
ti = 0.4 # this is the interlayer hopping (in terms of the intralayer)
from specialhopping import twisted_matrix
h = g.get_hamiltonian(is_sparse=True,has_spin=False,is_multicell=True,
     mgenerator=twisted_matrix(ti=ti))



hk = h.get_hk_gen() # get Bloch Hamiltonian generator

# hk is a function that given a k point, returns the Bloch Hamiltonian
# The k points are in the interval [0.,1.]


# This method automatically computes the local density of states
h.get_ldos(e=0.0) # e is the energy
# This method automatically computes the bands
#h.get_bands(num_bands=20)
