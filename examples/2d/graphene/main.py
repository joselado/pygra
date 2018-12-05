
import sys
import os
sys.path.append(os.environ["PYGRAROOT"])  # add pygra library

from pygra import geometry
from pygra import topology
from pygra import klist

g = geometry.honeycomb_lattice()
h = g.get_hamiltonian(has_spin=True)
h.shift_fermi(g.z+2.)

h.get_bands()
#dos.dos(h,nk=100,use_kpm=True)
