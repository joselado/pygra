
import sys
sys.path.append("../../../pygra")  # add pygra library

import geometry
import topology
import klist

g = geometry.honeycomb_lattice()
h = g.get_hamiltonian(has_spin=False)
#h.add_haldane(0.05)
#h.add_zeeman(0.3)
#h.add_rashba(0.3)
import parallel
parallel.cores = 3
h.add_sublattice_imbalance(0.6)
import dos
import topology
#op = h.get_operator("valley",projector=True) # valley operator
op = None
#topology.write_berry(h,mode="Green",operator=op,delta=0.00001)
op = None
#topology.berry_map(h,operator=op,delta=0.01,nk=60)
(x1,y1) = topology.write_berry(h,mode="Wilson",operator=op)
(x,y) = topology.write_berry(h,mode="Green",operator=op)
import matplotlib.pyplot as plt
plt.plot(x,y)
plt.scatter(x1,y1)
plt.show()

#c = topology.chern(h,mode="Green",delta=0.00001,nk=20)
#print("")
#print(c)
#h.get_bands()
#dos.dos(h,nk=100,use_kpm=True)
