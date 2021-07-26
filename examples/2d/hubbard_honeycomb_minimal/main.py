# Add the root path of the pygra library
import os ; import sys 
sys.path.append(os.path.dirname(os.path.realpath(__file__))+"/../../../src")





# zigzag ribbon
import numpy as np
from pygra import geometry
from pygra import scftypes
from scipy.sparse import csc_matrix
g = geometry.honeycomb_lattice()
g = g.supercell(1)
h = g.get_hamiltonian() # create hamiltonian of the system
mf = scftypes.guess(h,mode="antiferro")
U = 3.0
from pygra import scftypes
from pygra import meanfield
hubbard = meanfield.hubbardscf
filling = 0.5
mf = meanfield.guess(h,mode="antiferro")
scf = hubbard(h,nk=5,U=U,filling=filling,mf=mf,solver="plain",maxerror=1e-5,
        verbose=1)
#scf = hubbard(h,nk=10,U=U,filling=filling,mf=scf.mf,solver="broyden1")
h = scf.hamiltonian # get the Hamiltonian
#h.write_magnetization()
print(scf.identify_symmetry_breaking())
h.get_bands() # calculate band structure






