# Add the root path of the pygra library
import os ; import sys 
sys.path.append(os.path.dirname(os.path.realpath(__file__))+"/../../../src")





# zigzag ribbon
from pygra import geometry
import numpy as np
from pygra import embedding
g = geometry.honeycomb_lattice() # create geometry of a chain
#g = geometry.square_lattice() # create geometry of a chain
h = g.get_hamiltonian(has_spin=False) # get the Hamiltonian,spinless
# create a new intraterm, vacancy is modeled as a large onsite potential
#h.shift_fermi(2.0)
vintra = h.intra.copy() ; vintra[0,0] = 1000.0
from pygra import parallel
#parallel.cores = 7
eb = embedding.Embedding(h,m=vintra)
eb.multildos(nsuper=3)






