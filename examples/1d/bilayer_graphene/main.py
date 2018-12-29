# Add the root path of the pygra library
import os ; import sys ; sys.path.append(os.environ['PYGRAROOT'])

import numpy as np
from pygra import geometry
from pygra import hamiltonians
from pygra import ribbon
from pygra import multilayers
g = multilayers.get_geometry("AB",armchair=False) # bilayer AB geometry
g = ribbon.bulk2ribbon(g,n=20,clean=False) # get the geometry of a ribbon
#g = g.supercell(3)
#g.write() ; exit()
fun = multilayers.multilayer_hopping(ti=0.3) # function for the hopping
h = g.get_hamiltonian(has_spin=False,fun=fun) # create Hamiltonian
def ff(r): return r[2]*0.2 # interlayer bias
h.shift_fermi(ff) # add electric field
h.get_bands()
