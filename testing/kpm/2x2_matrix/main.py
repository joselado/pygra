import kpm # kernel polynomial method
import numpy as np
import pylab as py

m = np.matrix([[0.,1.],[1.,0.]]) # default matrix
m = m/2
mus = kpm.full_trace(m) # full trace
points = 200 # number of polynomials
x = np.linspace(-.9,.9,points*10)
y = kpm.generate_profile(mus,x)
py.plot(x,y)
py.show()
