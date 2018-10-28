
import sys
sys.path.append("../../../pygra")  # add pygra library

import geometry
import topology
import klist

g = geometry.triangular_lattice()
#g = geometry.honeycomb_lattice()
h = g.get_hamiltonian(has_spin=True)
h.shift_fermi(1.5)
#h.set_filling(0.1)
import response
response.magnetic_response_map(h,nk=60,nq=20)
#h.get_bands()
#dos.dos(h,nk=100,use_kpm=True)
