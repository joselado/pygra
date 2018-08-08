import kpm # kernel polynomial method
import numpy as np
import pylab as py
import time
from numpy.random import random

import geometry

g = geometry.honeycomb_lattice()
nrep = 2
g = g.supercell(nrep)
h = g.get_hamiltonian()

m = h.intra
m = m/6.
points = 10000 # number of polynomials
t1 = time.clock()
musp = kpm.full_trace(m,use_fortran=False) # full trace
t2 = time.clock()
musf = kpm.full_trace(m,use_fortran=True) # full trace
t3 = time.clock()
print "FORTRAN ",t3-t2
print "Python  ",t2-t1

x = np.linspace(-.9,.9,points*10)
t1 = time.clock()
yp = kpm.generate_profile(musp,x,use_fortran=False) # python
t2 = time.clock()
yf = kpm.generate_profile(musf,x,use_fortran=True) # fortran
t3 = time.clock()
print "FORTRAN ",t3-t2
print "Python  ",t2-t1
py.scatter(x,yp,label="Python",c="blue")
py.plot(x,yf,label="FORTRAN",c="green")
py.legend()
py.show()
