# Add the root path of the pygra library
import os ; import sys 
sys.path.append(os.path.dirname(os.path.realpath(__file__))+"/../../../src")





# zigzag ribbon
import numpy as np
from pygra import geometry
from pygra import hamiltonians
g = geometry.honeycomb_lattice()
  
h = g.get_hamiltonian() # create hamiltonian of the system
h.save() # save the Hamiltonian
del h # delete the Hamiltonian
h1 = hamiltonians.load() # load the Hamiltonian
h1.get_bands() # get the bandstructure






