import geometry  # library to create crystal geometries
import hamiltonians  # library to work with hamiltonians
import heterostructures
import numpy as np
import klist
import pylab as py
import green
import interactions


g = geometry.square_ribbon(4) # create geometry of the system
g = geometry.honeycomb_zigzag_ribbon(1) # create geometry of the system
h = g.get_hamiltonian() # create hamiltonian
hr = h.copy()
hl = h.copy()


es = np.linspace(-3.,3.,100) # array with the energies

hlist = [h for i in range(10)]  # create a list with the hamiltonians 
                                # of the scattering centrl part
# create a junction object
ht = heterostructures.create_leads_and_central_list(hr,hl,hlist) 
ht.block2full()
# calculate transmission
figt = ht.plot_landauer(energy=es,delta=0.00001,has_eh=h.has_eh)  # figure with the transmission
figb = h.plot_bands(nkpoints=300)  # figure with the bands
py.show()
