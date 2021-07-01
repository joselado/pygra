# Add the root path of the pygra library
import os ; import sys ; sys.path.append(os.environ['PYGRAROOT'])

import numpy as np
from pygra import geometry
from pygra import meanfield

# this example performs a selconsistent calculation in a dimer

g = geometry.lieb_lattice() # generate the geometry
g = g.supercell(2)
mz = [] # lists to store magnetizations
h = g.get_hamiltonian() # create hamiltonian of the system
h.add_rashba(1.0) # add Rashba spin-orbit coupling
#h.get_bands() ; exit()
mf = meanfield.guess(h,mode="random") # antiferro initialization
scf = meanfield.hubbardscf(h,filling=0.5,U=1.0,mf=mf,nk=5,verbose=1) # perform SCF
scf.hamiltonian.write_magnetization(nrep=2) # write selfconsistent magnetization
scf.hamiltonian.get_bands(operator="sx")
