
import sys
import os
sys.path.append(os.environ["PYGRAROOT"])  # add pygra library

from pygra import geometry

g = geometry.diamond_lattice_minimal()
h = g.get_hamiltonian(has_spin=True)
h1 = h.copy()
h2 = h.copy()
h1.add_antiferromagnetism(0.5)
h2.add_antiferromagnetism(-0.5)

from pygra import kdos
kdos.interface(h1,h2)
