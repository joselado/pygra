import kpm # kernel polynomial method
import numpy as np
import pylab as py
import time
from numpy.random import random

m = np.matrix([[0.,1.],[1.,0.]]) # default matrix
ndim = 30
m = np.matrix(random((ndim,ndim))) -1.
m += m.H
m = m/(2*ndim)
points = 200 # number of polynomials
t1 = time.clock()
musp = kpm.full_trace(m,use_fortran=False) # full trace
t2 = time.clock()
musf = kpm.full_trace(m,use_fortran=True) # full trace
t3 = time.clock()
print "FORTRAN ",t3-t2
print "Python  ",t2-t1

x = np.linspace(-.9,.9,points*10)
yp = kpm.generate_profile(musp,x) # python
yf = kpm.generate_profile(musf,x) # fortran
py.plot(x,yp,label="Python")
py.plot(x,yp,label="FORTRAN")
py.legend()
py.show()
