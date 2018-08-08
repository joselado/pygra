import geometry  # library to create crystal geometries
import hamiltonians  # library to work with hamiltonians
import islands
import numpy as np
import sculpt
import pylab as py
import kpm
import correlator

g = geometry.chain()
g = g.supercell(10)
g.dimensionality = 0
g = islands.get_geometry(name="honeycomb",rot=np.pi/3,nedges=3,n=20)
h = g.get_hamiltonian(has_spin=False)

i = sculpt.get_central(g,n=1)[0]
print(g.r[i])
d = correlator.gij(h.intra,i=i)
np.savetxt("CORR.OUT",np.matrix([g.x,g.y,d]).T)
#(x,y,yi) = kpm.correlator0d(h.intra,npol=200,i=0,j=4)
#correlator.correlator0d(h.intra,i=0,j=4)
#print(np.trapz(y,x=x,dx=x[1]-x[0]))

