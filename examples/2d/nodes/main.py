# Add the root path of the pygra library
import os ; import sys ; sys.path.append(os.environ['PYGRAROOT'])

from pygra import geometry
from pygra import nodes
g = geometry.honeycomb_lattice()
h = g.get_hamiltonian(has_spin=False)
k = nodes.degenerate_points(h,n=len(g.r)//2-1) 
print(k)
nodes.dirac_points(h,n=len(g.r)//2-1) 
