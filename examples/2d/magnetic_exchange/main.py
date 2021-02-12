# Add the root path of the pygra library
import os ; import sys ; sys.path.append(os.environ['PYGRAROOT'])

from pygra import geometry
g = geometry.triangular_lattice()
h = g.get_hamiltonian(has_spin=True)
h.set_filling(0.05,nk=10)
from pygra import magneticexchange
J = magneticexchange.NN_exchange(h,nk=100,J=1,mode="spiral",filling=0.5)
print("Exchange is",J)
