import geometry  # library to create crystal geometries
import hamiltonians  # library to work with hamiltonians
import hexagonal

g = geometry.honeycomb_lattice()
g = g.supercell(3)
h = g.get_hamiltonian()
h = hexagonal.honeycomb2square(h)
h = hexagonal.bulk2ribbon(h,n=10)
h.write()
