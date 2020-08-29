# Add the root path of the pygra library
import os ; import sys ; sys.path.append(os.environ['PYGRAROOT'])

from pygra import specialhamiltonian
from pygra import geometry
g = geometry.triangular_lattice()
g = g.supercell(3)
h = specialhamiltonian.valence_TMDC(soc=0.1,g=g)
h.write_hopping()
h.get_bands()
