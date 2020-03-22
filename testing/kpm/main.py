import kpm # kernel polynomial method
import numpy as np
import pylab as py
import time
from numpy.random import random

import geometry

g = geometry.chain()
nrep = 40
g = g.supercell(nrep)
h = g.get_hamiltonian()

m = h.intra
m = m/6.
points = 200 # number of polynomials
t1 = time.perf_counter()
musp = kpm.full_trace(m,use_fortran=False) # full trace
t2 = time.perf_counter()
musf = kpm.full_trace(m,use_fortran=True) # full trace
t3 = time.perf_counter()
print "FORTRAN ",t3-t2
print "Python  ",t2-t1

x = np.linspace(-.9,.9,points*10)
yp = kpm.generate_profile(musp,x) # python
yf = kpm.generate_profile(musf,x) # fortran
py.scatter(x,yp,label="Python",c="blue")
py.plot(x,yf,label="FORTRAN",c="green")
py.legend()
py.show()
