# Add the root path of the pygra library
import os ; import sys ; sys.path.append(os.environ['PYGRAROOT'])

import numpy as np
from pygra import geometry
g = geometry.diamond_lattice_minimal()
from pygra import films
g = films.geometry_film(g,nz=5)
g.write()
h = g.get_hamiltonian()
h.get_bands()
