# Add the root path of the pygra library
import os ; import sys ; sys.path.append(os.environ['PYGRAROOT'])

import numpy as np
from pygra import geometry
from pygra import topology
g = geometry.honeycomb_lattice()
h = g.get_hamiltonian(has_spin=False)
#h = g.get_hamiltonian()
#h.add_rashba(0.5)
#h.add_zeeman([0.,0.,0.5])
h.shift_fermi(0.5)
h.add_haldane(0.1)
topology.berry_density_map(h,nk=200)
#parallel.cores = 7
#topology.chern_density(h,es=np.linspace(-5.0,5.0,200),nk=10)
#topology.write_berry(h,mode="Green")
h.get_bands()
#dos.dos(h,nk=100,use_kpm=True)
