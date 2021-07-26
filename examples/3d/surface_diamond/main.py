# Add the root path of the pygra library
import os ; import sys 
sys.path.append(os.path.dirname(os.path.realpath(__file__))+"/../../../src")





from pygra import geometry
from pygra import dos
g = geometry.diamond_lattice_minimal()
h = g.get_hamiltonian()
#h.add_antiferromagnetism(1.)
dos.bulkandsurface(h,nk=300,delta=0.01)
#h.get_bands()






