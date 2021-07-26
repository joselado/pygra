# Add the root path of the pygra library
import os ; import sys 
sys.path.append(os.path.dirname(os.path.realpath(__file__))+"/../../../src")





from pygra import geometry
from pygra import heterostructures
import numpy as np
g = geometry.square_ribbon(3)
h = g.get_hamiltonian()
ht = heterostructures.create_leads_and_central(h,h,h)
h.get_bands() # get bandstructure
es = np.linspace(-1.,1.,50)
ts = [ht.landauer(e) for e in es]
np.savetxt("TRANSPORT.OUT",np.matrix([es,ts]).T)






