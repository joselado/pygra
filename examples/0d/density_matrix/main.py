# Add the root path of the pygra library
import os ; import sys 
sys.path.append(os.path.dirname(os.path.realpath(__file__))+"/../../../src")





from pygra import islands
from pygra import densitymatrix
import numpy as np
import time
g = islands.get_geometry(name="honeycomb",n=4,clean=False) # get an island
h = g.get_hamiltonian() # get the Hamiltonian
h.add_rashba(.2)
h.add_zeeman([0.,0.,0.3])
g.write()
t1 = time.clock()
dm = densitymatrix.full_dm(h,use_fortran=False)
t2 = time.clock()
dmf = densitymatrix.full_dm(h,use_fortran=True)
t3 = time.clock()
print("Error = ",np.sum(np.abs(dm-dmf)))
print("Time Fortran = ",t3-t2)
print("Time Python = ",t2-t1)






