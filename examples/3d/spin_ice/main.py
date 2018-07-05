import sys
import numpy as np
import os
sys.path.append(os.environ["PYGRAROOT"])

import geometry
import sculpt

g = geometry.pyrochlore_lattice()
h = g.get_hamiltonian()
h.add_antiferromagnetism(1.0)
h.write_magnetization()
