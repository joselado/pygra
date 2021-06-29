# Add the root path of the pygra library
import os ; import sys ; sys.path.append(os.environ['PYGRAROOT'])

import numpy as np
from pygra import geometry
from pygra import meanfield

# this example performs a selconsistent calculation in a dimer

g = geometry.lieb_lattice() # generate the geometry
Us = np.linspace(0.,2.,20) # different Hubbard U
mz = [] # lists to store magnetizations
for U in Us: # loop over Hubbard U
    h = g.get_hamiltonian() # create hamiltonian of the system
    mf = meanfield.guess(h,mode="antiferro") # antiferro initialization
    scf = meanfield.hubbardscf(h,filling=0.5,U=U,mf=mf,nk=5) # perform SCF
    mz0 = scf.hamiltonian.compute_vev("sz",nk=5) # expectation value
    mz.append(np.sum(np.abs(mz0))) # total magentization

# now plot all the results

import matplotlib.pyplot as plt

plt.plot(Us,mz,marker="o",label="Site #1",c="red") 
plt.legend()
plt.xlabel("Hubbard U")
plt.ylabel("Magnetic moment")
plt.show()



