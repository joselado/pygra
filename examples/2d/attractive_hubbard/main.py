# Add the root path of the pygra library
import os ; import sys ; sys.path.append(os.environ['PYGRAROOT'])

# zigzag ribbon
import numpy as np
from pygra import geometry
from pygra import scftypes
from scipy.sparse import csc_matrix
from pygra import meanfield
g = geometry.honeycomb_lattice()
h = g.get_hamiltonian() # create hamiltonian of the system
h.add_swave(0.0)
U = -2.0
#hubbard = scftypes.hubbardscf

mf = meanfield.guess(h,mode="random")
scf = meanfield.Vinteraction(h,nk=4,U=U,filling=0.7,mf=mf,
        constrains = ["no_normal_term"])
h = scf.hamiltonian # get the Hamiltonian
print(scf.identify_symmetry_breaking())
h.get_bands(operator="electron") # calculate band structure
