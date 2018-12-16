from pygra import geometry
from pygra import dos

g = geometry.diamond_lattice()

h = g.get_hamiltonian()
h.turn_dense()
h.add_antiferromagnetism(1.)

dos.dos3d(h,nk=30,delta=0.001,random=True,ndos=1000)
h.get_bands()
