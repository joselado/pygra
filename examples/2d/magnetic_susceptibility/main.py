
import sys
sys.path.append("../../../pygra")  # add pygra library

import geometry
import topology
import klist

g = geometry.triangular_lattice()
h = g.get_hamiltonian(has_spin=True)
h.shift_fermi(1.5)
h.turn_dense()
h.set_filling(0.1)
import response
response.magnetic_response_map(h,nk=20,nq=40)
#h.get_bands()
#dos.dos(h,nk=100,use_kpm=True)
