# Add the root path of the pygra library
import os ; import sys ; sys.path.append(os.environ['PYGRAROOT'])

import numpy as np
from pygra import geometry
g = geometry.pyrochlore_lattice()
#g = geometry.kagome_lattice()
from pygra import films
g = films.geometry_film(g,nz=1)
#g = g.supercell(3)
#g.write()
#exit()
#g = ribbon.bulk2ribbon(g)
h = g.get_hamiltonian()
h.shift_fermi(1.5)
h.get_bands()
exit()
from pygra import scftypes
mf = scftypes.guess(h,mode="random")
scf = scftypes.selfconsistency(h,nkp=10,filling=0.5,g=1.5,
                mix=0.9,mf=mf,mode="U")
scf.hamiltonian.get_bands()
