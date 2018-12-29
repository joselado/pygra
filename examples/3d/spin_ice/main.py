# Add the root path of the pygra library
import os ; import sys ; sys.path.append(os.environ['PYGRAROOT'])

import numpy as np
from pygra import geometry
from pygra import sculpt
g = geometry.pyrochlore_lattice()
h = g.get_hamiltonian()
h.add_antiferromagnetism(1.0)
h.write_magnetization()
