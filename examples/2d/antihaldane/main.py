
import sys
sys.path.append("../../../pygra")  # add pygra library

import geometry
import topology
import klist

g = geometry.honeycomb_lattice()
h = g.get_hamiltonian(has_spin=True)

#h.clean()
h.add_zeeman(0.2)
h.add_modified_haldane(0.1)
h.add_swave(0.1)
h.get_bands(operator=h.get_operator("sz"))

#h.get_bands(operator=h.get_operator("valley"))
