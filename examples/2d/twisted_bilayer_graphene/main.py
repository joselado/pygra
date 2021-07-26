# Add the root path of the pygra library
import os ; import sys 
sys.path.append(os.path.dirname(os.path.realpath(__file__))+"/../../../src")




from pygra import specialgeometry
from pygra.specialhopping import twisted_matrix
g = specialgeometry.twisted_bilayer(3)
h = g.get_hamiltonian(mgenerator=twisted_matrix(ti=0.12))
h.get_bands(nk=100)







