# zigzag ribbon
import sys
sys.path.append("../../../pygra")  # add pygra library

import geometry
import numpy as np
import embedding

# Here we will use the embedding method to calculate the
# density of states of a single vacancy in infinite graphene

# The embedding technique is a quite expensive algorithm, if you use
# large cells it will take a lot of time

g = geometry.honeycomb_lattice() # create geometry of a chain
h = g.get_hamiltonian(has_spin=False) # get the Hamiltonian,spinless

# create a new intraterm, vacancy is modeled as a large onsite potential

vintra = h.intra.copy() ; vintra[0,0] = 1000.0

energies = np.linspace(-3.5,3.5,200)
delta = 0.01 # smearing
embedding.dos_impurity(h,vc=vintra,silent=False,energies=energies,
                      delta=delta,use_generator=False)

# results are written in DOS_DEFECTIVE.OUT and DOS_PRISTINE.OUT
