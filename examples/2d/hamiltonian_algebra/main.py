# Add the root path of the pygra library
import os ; import sys ; sys.path.append(os.environ['PYGRAROOT'])

# zigzag ribbon
import numpy as np
from pygra import geometry
from scipy.sparse import csc_matrix
from pygra import meanfield
g = geometry.honeycomb_lattice()
h = g.get_hamiltonian(has_spin=True) # create hamiltonian of the system
h = h + h
h.get_bands()
