# zigzag ribbon
import sys
import os
sys.path.append("../../../pygra")  # add pygra library
import numpy as np
import geometry
import hamiltonians
g = geometry.honeycomb_lattice()


  
h = g.get_hamiltonian() # create hamiltonian of the system
h.save() # save the Hamiltonian
del h # delete the Hamiltonian
h1 = hamiltonians.load() # load the Hamiltonian
h1.get_bands() # get the bandstructure
