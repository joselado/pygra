import geometry
import hamiltonians


g = geometry.honeycomb_lattice()
g = g.supercell(20)
g.dimensionality = 0

h = g.get_hamiltonian()

h.remove_spin()

import neighbor
pairs = neighbor.find_first_neighbor(g.r,g.r)

print pairs

h.write()

