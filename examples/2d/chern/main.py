# Add the root path of the pygra library
import os ; import sys ; sys.path.append(os.environ['PYGRAROOT'])

from pygra import geometry
from pygra import topology
from pygra import klist
from pygra import dos
from pygra import topology
g = geometry.honeycomb_lattice()
h = g.get_hamiltonian(has_spin=False)
h.add_haldane(0.05)
c = topology.chern(h)
print(c)
#dos.dos(h,nk=100,use_kpm=True)
