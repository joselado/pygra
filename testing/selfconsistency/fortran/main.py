import geometry
import sculpt

g = geometry.square_lattice()
g = g.supercell(8)

h = g.get_hamiltonian()
h.remove_spin()

import interactions
import numpy as np
#mag_ini = np.array([-1,1,-1,1])
mag_ini = None
interactions.hubbard0d(h.intra,mixing=0.9,mag_ini=mag_ini,U=1.0,info=True)
