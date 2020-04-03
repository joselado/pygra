# Add the root path of the pygra library
import os ; import sys ; sys.path.append(os.environ['PYGRAROOT'])

from pygra import islands
import numpy as np
g = islands.get_geometry(name="honeycomb",n=10,nedges=4,rot=0.0,clean=False) 
h = g.get_hamiltonian(has_spin=False)
h.add_haldane(lambda r: 0.1)
from pygra import topology
topology.real_space_chern(h)
