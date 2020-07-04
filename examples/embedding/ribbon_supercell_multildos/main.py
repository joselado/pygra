# Add the root path of the pygra library
import os ; import sys ; sys.path.append(os.environ['PYGRAROOT'])

# zigzag ribbon
from pygra import geometry
import numpy as np
from pygra import embedding
g = geometry.honeycomb_armchair_ribbon(30)
h = g.get_hamiltonian(has_spin=False) # get the Hamiltonian,spinless
h.add_peierls(.05)
# create a new intraterm, vacancy is modeled as a large onsite potential
ii = g.get_central()
vintra = h.intra.copy() ; vintra[ii,ii] = 1000.0
eb = embedding.Embedding(h,m=vintra)
eb.multildos(nsuper=5,es=np.linspace(-.5,.5,100))
