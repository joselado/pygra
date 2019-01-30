# Add the root path of the pygra library
import os ; import sys ; sys.path.append(os.environ['PYGRAROOT'])

from pygra import islands
from pygra import interactions
from pygra import scftypes
import numpy as np
g = islands.get_geometry(name="honeycomb",n=7,nedges=3,rot=np.pi/3) # get an island
h = g.get_hamiltonian() # get the Hamiltonian
g.write()
scf = scftypes.hubbardscf(h,g=1.0,mag=[[0,0,1] for r in g.r])
scf.hamiltonian.get_bands()
