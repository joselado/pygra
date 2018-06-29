import sys
sys.path.append("../../../pygra")  # add pygra library
import geometry
import topology

g = geometry.honeycomb_lattice()
h = g.get_hamiltonian(has_spin=False)
h.add_sublattice_imbalance(0.1)
op = h.get_operator("valley",projector=True) # valley operator
c = topology.chern(h,mode="Green",delta=0.0001,nk=20,operator=op)
print("")
print(c)

