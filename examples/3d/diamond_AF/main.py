import sys
sys.path.append("../../../pygra")  # add pygra library

import geometry
import dos

g = geometry.diamond_lattice()

h = g.get_hamiltonian()
h.add_antiferromagnetism(1.)

dos.dos3d(h,nk=30,delta=0.001,random=True,ndos=1000)
h.get_bands()
