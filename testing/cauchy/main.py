import geometry  # library to create crystal geometries
import hamiltonians  # library to work with hamiltonians
import input_tb90 as in90
import heterostructures
import sys
import sculpt  # to modify the geometry
import numpy as np
import klist
import pylab as py
import green

g = geometry.square_ribbon(4) 
h = hamiltonians.hamiltonian(g) # create hamiltonian
h.first_neighbors()  # create first neighbor hopping
#h.set_finite()

#h.add_zeeman([0.,0.,-1])
h.remove_spin()

dx = -6.0
dy = 6j

ne = 100
e1 = np.linspace(dx,dx+dy,ne)
e2 = np.linspace(dx+dy,dy,ne)
e3 = np.linspace(dy,0.0,ne)
e4 = np.linspace(0.0,dx,ne)

de1 = dy/ne
de2 = -dx/ne
de3 = -de1
de4 = -de2

def f(x):
#  return np.exp(-x) 
  return 1/(x*x+100)
  return np.sin(x)


ecs = [e1,e2,e3,e4]
ecs = [e1,e2,e3]
#ecs = [e4]
des = [de1,de2,de3,de4]
des = [de1,de2,de3]
#des = [de4]

gt = h.intra*0.0
gt2 = h.intra*0.0

#gt = 0.0

i = np.identity(len(h.intra))
for (e,de) in zip(ecs,des):
  for ie in e:
#    g = ((ie+0.001j)*i - h.intra).I
    g,s = green.bloch_selfenergy(h,energy = ie,mode="renormalization")
#    gt += f(ie)*de
    gt += g*de



print "Integral of DOS from",dx,"to  0"
print -gt.trace()[0,0].imag/np.pi
#print gt
