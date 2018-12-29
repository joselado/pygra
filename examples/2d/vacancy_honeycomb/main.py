# Add the root path of the pygra library
import os ; import sys ; sys.path.append(os.environ['PYGRAROOT'])

from pygra import geometry
from pygra import topology
from pygra import dos
from pygra import operators
g = geometry.honeycomb_lattice()
g = g.supercell(2)
g = g.remove(0)
h = g.get_hamiltonian(has_spin=True)
f = operators.get_inplane_valley(h)
h.get_bands(operator=f)
#dos.dos(h,nk=100,use_kpm=True)
