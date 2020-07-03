# Add the root path of the pygra library
import os ; import sys ; sys.path.append(os.environ['PYGRAROOT'])

from pygra import geometry
from pygra import topology
from pygra import dos
g = geometry.honeycomb_lattice()
#g = geometry.honeycomb_lattice_C6()
#g = geometry.chain()
g = g.supercell(3)
g.write()
h = g.get_hamiltonian(has_spin=False)
h = h.get_multicell()
h.add_kekule(0.4)
#h.add_haldane(0.3)
#h1 = h.copy() ; h1.clean() ; h1.add_haldane(0.3) ; h.add_hamiltonian(h1)
h.get_bands(operator="valley_x")
from pygra import groundstate
groundstate.hopping(h,nrep=2) # write three replicas
