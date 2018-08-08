import geometry  # library to create crystal geometries
import hamiltonians  # library to work with hamiltonians
import input_tb90 as in90
import numpy as np
import pylab as py
import tojulia


#g = geometry.honeycomb_lattice()  # create a honeycomb lattice
g = geometry.square_ribbon(1) 
g = g.supercell(3)  # double supercell
h = g.get_hamiltonian()
h.write()
h.remove_spin()
tojulia.write_hamiltonian(h)
#fig = h.plot_bands()

#py.show()
