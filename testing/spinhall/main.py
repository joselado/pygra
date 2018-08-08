import geometry
import numpy as np
import matplotlib.pyplot as plt
import operators


g = geometry.honeycomb_lattice()

h = g.get_hamiltonian()

h.add_kane_mele(0.01)
h.add_sublattice_imbalance(0.8)
#h.add_zeeman([0.,0.,0.6])
#h.add_rashba(0.05)
import topology
import multicell
#h = multicell.turn_multicell(h)


import bandstructure


#print topology.precise_spin_chern(h,delta=0.0001)
#print topology.spin_chern(h,delta=0.0001,nk=50)
#print topology.chern(h,nk=100)


klist = [(i,i) for i in np.linspace(0.,1.0,600)] # list of kpoints

bandstructure.berry_bands(h,klist=klist,mode="sz")
exit()
topology.write_berry(h,klist,dk=0.0001)
topology.write_spin_berry(h,klist,delta=0.00001)

