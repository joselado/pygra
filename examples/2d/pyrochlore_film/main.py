import numpy as np
from pygra import geometry

g = geometry.pyrochlore_lattice()
from pygra import films
g = films.geometry_film(g,nz=10)
h = g.get_hamiltonian()
h.add_kane_mele(0.1)
h.turn_dense()
h.get_bands(operator="zposition")


