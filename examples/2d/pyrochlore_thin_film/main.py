# Add the root path of the pygra library
import os ; import sys 
sys.path.append(os.path.dirname(os.path.realpath(__file__))+"/../../../src")





import numpy as np
from pygra import geometry
g = geometry.pyrochlore_lattice()
g.write()
from pygra import films
g = films.geometry_film(g,nz=1)
h = g.get_hamiltonian()
h.shift_fermi(1.5)
h.get_bands()






