# Add the root path of the pygra library
import os ; import sys 
sys.path.append(os.path.dirname(os.path.realpath(__file__))+"/../../../src")




from pygra import specialgeometry
import numpy as np
from pygra import geometry,spectrum

g = geometry.honeycomb_lattice()
h = g.get_hamiltonian(has_spin=True)
h.add_sublattice_imbalance(0.3) # opena gap
h.add_rashba(.2) # and add Rashba
#h.set_filling(0.,nk=1)


# now define the two operators you want
ops = [h.get_operator("sx"),h.get_operator("sy")]
# and compute their expactation values
n = [1] # index of the band above the fermi energy you want
spectrum.selected_bands2d(h,nindex=n,operator=ops,nsuper=1,nk=20)







