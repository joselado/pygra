# Add the root path of the pygra library
import os ; import sys 
sys.path.append(os.path.dirname(os.path.realpath(__file__))+"/../../../src")





from pygra importgeometry
import topology
import klist
g = geometry.honeycomb_lattice()
h = g.get_hamiltonian(has_spin=False)
h.add_sublattice_imbalance(0.5)
from pygra importdos
import topology
topology.berry_map(h,mode="Green")
#h.get_bands()
#dos.dos(h,nk=100,use_kpm=True)






