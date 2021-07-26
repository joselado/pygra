# Add the root path of the pygra library
import os ; import sys 
sys.path.append(os.path.dirname(os.path.realpath(__file__))+"/../../../src")





from pygra import geometry
from pygra import films
g = geometry.diamond_lattice_minimal()
g = films.geometry_film(g,nz=20)
h = g.get_hamiltonian()
h.get_bands()







