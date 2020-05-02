# Add the root path of the pygra library
import os ; import sys ; sys.path.append(os.environ['PYGRAROOT'])

from pygra import geometry
from pygra import topology
g = geometry.honeycomb_lattice()
h = g.get_hamiltonian(has_spin=True)
h.add_antiferromagnetism(0.6)
from pygra import topology
topology.parallel.cores = 6

op = h.get_operator("valley")*h.get_operator("sz") # valley operator
(x1,y1) = topology.write_berry(h)
(x,y) = topology.write_berry(h,operator=op)
import matplotlib.pyplot as plt
plt.plot(x,y,c="blue",label="Valley Spin Berry")
plt.scatter(x1,y1,c="red",label="Berry")
plt.legend()
plt.show()
