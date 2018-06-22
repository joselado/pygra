
import sys
sys.path.append("../../../pygra")  # add pygra library
import islands
import interactions
import numpy as np

g = islands.get_geometry(name="honeycomb",n=4,nedges=3,rot=np.pi/3) # get an island
h = g.get_hamiltonian() # get the Hamiltonian
g.write()

import scftypes
scf = scftypes.hubbardscf(h,U=1.0,mag=[[0,0,1] for r in g.r])
scf.hamiltonian.get_bands()
