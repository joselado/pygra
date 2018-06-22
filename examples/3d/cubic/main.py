import sys
sys.path.append("../../../pygra")  # add pygra library

import geometry
import dos

g = geometry.cubic_lattice()

h = g.get_hamiltonian()

# A well converged DOS requires more k-points
h.turn_dense()
dos.dos3d(h,nk=10,delta=0.1,random=False,ndos=1000)
