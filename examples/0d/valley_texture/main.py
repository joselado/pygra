# Add the root path of the pygra library
import os ; import sys ; sys.path.append(os.environ['PYGRAROOT'])

from pygra import islands
from pygra import spectrum
from pygra import operators

import numpy as np
g = islands.get_geometry(name="honeycomb",n=8,nedges=6,rot=0.0) # get an island
i = g.get_central()[0]
#g = g.remove(i)

h = g.get_hamiltonian(has_spin = False)
h.add_peierls(0.05)
#h.add_sublattice_imbalance(0.1)
ops = operators.get_envelop(h,sites=range(h.intra.shape[0]),d=0.3)

fv = operators.get_valley(h,projector=True) # valley function
#fv = operators.get_valley_taux(h,projector=True) # valley function
ops = [fv()@o for o in ops] # local times valley

ys = spectrum.ev(h,operator=ops).real

np.savetxt("EV.OUT",np.array([g.x,g.y,ys]).T)



