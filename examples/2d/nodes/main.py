
import sys
sys.path.append("../../../pygra")  # add pygra library

import geometry
import nodes

g = geometry.honeycomb_lattice()
h = g.get_hamiltonian(has_spin=False)
k = nodes.degenerate_points(h,n=len(g.r)//2-1) 
print(k)
nodes.dirac_points(h,n=len(g.r)//2-1) 
