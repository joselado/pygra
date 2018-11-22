
import sys
sys.path.append("../../../pygra")  # add pygra library

import geometry
import topology
import klist

g = geometry.triangular_lattice()
g = geometry.honeycomb_lattice()
h = g.get_hamiltonian(has_spin=True)
h.shift_fermi(0.6)
#h.set_filling(nk=20)
h.get_bands()
import spectrum
spectrum.fermi_surface(h)
