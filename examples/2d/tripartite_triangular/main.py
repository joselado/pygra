
import sys
sys.path.append("../../../pygra")  # add pygra library

import geometry
import topology
import klist

g = geometry.triangular_lattice_tripartite()
g = g.supercell(3)
g.write()
