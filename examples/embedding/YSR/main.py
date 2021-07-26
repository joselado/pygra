# Add the root path of the pygra library
import os ; import sys 
sys.path.append(os.path.dirname(os.path.realpath(__file__))+"/../../../src")





# zigzag ribbon
from pygra import geometry
import numpy as np
from pygra import embedding
g = geometry.honeycomb_lattice() # create geometry of a chain
#g = geometry.square_lattice() # create geometry of a chain
g = g.supercell(2) # supercell
h = g.get_hamiltonian(has_spin=True) # get the Hamiltonian,spinless
# create a new intraterm, vacancy is modeled as a large onsite potential

# put a vacancy
r0 = g.r[g.get_central()][0]

def f(r):
    dr = r-r0 ; dr = dr.dot(dr)
    if dr<1e-2: return 10000.0 # remove site
    return 0.0

def fm(r):
    dr = r-r0 ; dr = dr.dot(dr)
    if 0.9<dr<1.1: return [.0,.0,.2] # exchange
    return [0.,0.,0.]

h.add_swave(0.2)
hv = h.copy()
hv.add_zeeman(fm)
hv.add_onsite(f)
hv.add_onsite(lambda r: -fm(r)[2])
vintra = hv.intra
es = np.linspace(-0.3,0.3,200)

from pygra import parallel
parallel.cores = 6

op = h.get_operator("electron")*h.get_operator("dn")

eb = embedding.Embedding(h,m=vintra)
(es,ds) = eb.multidos(es=es,nsuper=1,delta=1e-2,operator=op)
import matplotlib.pyplot as plt
plt.plot(es,ds)
plt.show()






