# Add the root path of the pygra library
import os ; import sys ; sys.path.append(os.environ['PYGRAROOT'])

from pygra import geometry
from pygra import dos
g = geometry.honeycomb_lattice()
h = g.get_hamiltonian(has_spin=False)
dos.dos(h,mode="ED",delta=0.01,nk=100)
#dos.dos(h,nk=100,use_kpm=True)
