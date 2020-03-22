# Add the root path of the pygra library
import os ; import sys ; sys.path.append(os.environ['PYGRAROOT'])

from pygra import islands
from pygra import densitymatrix
import numpy as np
import time
g = islands.get_geometry(name="honeycomb",n=4,clean=False) # get an island
h = g.get_hamiltonian() # get the Hamiltonian
h.add_rashba(.2)
h.add_zeeman([0.,0.,0.3])
g.write()
t1 = time.perf_counter()
dm = densitymatrix.full_dm(h,use_fortran=False)
t2 = time.perf_counter()
dmf = densitymatrix.full_dm(h,use_fortran=True)
t3 = time.perf_counter()
print("Error = ",np.sum(np.abs(dm-dmf)))
print("Time Fortran = ",t3-t2)
print("Time Python = ",t2-t1)
