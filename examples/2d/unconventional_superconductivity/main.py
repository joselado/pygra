# Add the root path of the pygra library
import os ; import sys ; sys.path.append("../../../src/")

# zigzag ribbon
import numpy as np
from pygra import geometry
from scipy.sparse import csc_matrix
from pygra import meanfield
g = geometry.triangular_lattice()
h = g.get_hamiltonian() # create hamiltonian of the system

# We will take a ferromagnetic triangular lattice, whose
# superconducting state is a p-wave superfluid state with
# odd frequency superconductivity

h.add_zeeman([20.,0.,0.0]) # add ferromagnetism
h.turn_nambu() # setup a Nambu hamiltonian


# the interaction terms are controlled by U, V1 and V2
# U is the onsite Hubbard interaction
# V1 is the first neighbor charge-charge interaction
# V2 is the second neighbor charge-charge interaction
mf = meanfield.guess(h,"random") # random intialization
scf = meanfield.Vinteraction(h,U=0.0,V1=-6.0,V2=0.0,
        nk=20,filling=0.1,mf=mf,mix=0.3,
        compute_normal=False)
from pygra import scftypes



print("##########################################")
print("Symmetry breaking created by interactions")
print(scf.identify_symmetry_breaking())
print("##########################################")





# now extract the Hamiltonian and compute the bands
h = scf.hamiltonian # get the Hamiltonian
h.get_bands(operator="electron") # calculate band structure
