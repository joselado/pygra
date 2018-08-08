import geometry  # library to create crystal geometries
import hamiltonians  # library to work with hamiltonians
import numpy as np
import pylab as py
import multiterminal


g = geometry.square_ribbon(1) # create geometry of the system
h = g.get_hamiltonian() # create hamiltonian

d = multiterminal.device() # create device
l = multiterminal.lead() # create lead
l.intra, l.inter, l.coupling = h.intra, h.inter, h.inter # create arguments
d.leads = [l for i in range(10)]  # add the leads
d.center = h.intra # add central hamiltonian

ts = multiterminal.landauer(d,0.0,ij=[(0,1),(0,2)])
print ts

