# Add the root path of the pygra library
import os ; import sys ; sys.path.append(os.environ['PYGRAROOT'])

# zigzag ribbon
import numpy as np
from pygra import geometry
from pygra import scftypes
from scipy.sparse import csc_matrix
from pygra import meanfield
g = geometry.square_lattice() # square lattice
h = g.get_hamiltonian() # create hamiltonian of the system
h.add_swave(0.0) # activate a BdG Hamiltonian
mf = meanfield.guess(h,mode="random")
scf = meanfield.Vinteraction(h,
        nk=10, # number of k-points
        U=-0.2, # interaction strength for the onsite interaction
        filling=0.5, # filling of the system
        mf=mf, # initial guess (ranodm should be ok)
        mix = 0.8, # mixing of the SCF
        verbose=1, # this prints some info of the SCF
        constrains = ["no_normal_term"] # ignore normal terms of the SCF
        )
h = scf.hamiltonian # get the selfconsistent Hamiltonian
print(scf.identify_symmetry_breaking())
h.get_bands(operator="electron") # calculate band structure
