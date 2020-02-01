# Add the root path of the pygra library
import os ; import sys ; sys.path.append(os.environ['PYGRAROOT'])

from pygra import geometry
from pygra import ldos
import numpy as np

n = 40
w = n/2. # cutoff for the hopping
g = geometry.chain(n) # chain
g.dimensionality = 0

def f(r1,r2):
    i1 = g.get_index(r1)
    i2 = g.get_index(r2)
    if abs(i1-i2)==1: return 1.0
    elif abs(i1-i2)==3: return 1.0/3.
    else: return 0.0
#        i = min([i1,i2])
#        d = i#/w # value of the decay
#        return (w)/(d**2+w)
#    return 0.

h = g.get_hamiltonian(fun=f,has_spin=False)
#h = g.get_hamiltonian(has_spin=False)
ldos.multi_ldos(h,delta=2e-2,es=np.linspace(-0.5,0.5,300))

