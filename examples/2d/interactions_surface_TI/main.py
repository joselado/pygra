# zigzag ribbon
import sys
sys.path.append("../../../pygra")  # add pygra library

from surface_TI import geometry2hamiltonian # this function will yield the Hamiltonian

import geometry

g = geometry.single_square_lattice() # create the basic geometry
h = geometry2hamiltonian(g,mw=0.0) # get the Hamiltonian, mw is the Wilson mass


import scftypes

scf = scftypes.hubbardscf(h,U=1.,nkp=10,filling=0.5)

h = scf.hamiltonian
h.get_bands() # get the bandstructure
h.write()

