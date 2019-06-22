# Add the root path of the pygra library
import os ; import sys ; sys.path.append(os.environ['PYGRAROOT'])

from pygra import islands

import numpy as np
from pygra import geometry
g = islands.get_geometry(name="honeycomb",n=6,nedges=6,rot=0.) 
#g = geometry.bichain()
#g = g.supercell(100)
g.dimensionality = 0
h = g.get_hamiltonian(has_spin=False)
h.add_haldane(0.2)
#h.add_sublattice_imbalance(0.4)
#h.get_bands()
#exit()
#h.shift_fermi(0.1)
from pygra import timeevolution
from pygra import parallel
parallel.cores = 5
timeevolution.evolve_local_state(h,i=0,ts=np.linspace(0.,200,100))

