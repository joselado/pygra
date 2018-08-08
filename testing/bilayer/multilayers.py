# library to create multilayer systems
from copy import deepcopy
import numpy as np

def bilayer_aa(h,t = 0.1):
  """ Creates a bilayer from a honeycomb ribbon"""
  nlayers = 2 # number of layers
  g = h.geometry # get the geometry
  go = deepcopy(g) # copy the geometry
  go.x = [] 
  go.y = []
  go.z = []
  if g.name == "honeycomb_armchair_ribbon": dx ,dy = 1. ,0.
  if g.name == "honeycomb_zigzag_ribbon": dx ,dy = 0. ,-1.
  for (xi,yi) in zip(g.x,g.y):  # modify the geometry
    go.x.append(xi)
    go.x.append(xi+dx)
    go.y.append(yi)
    go.y.append(yi+dy)
    go.z.append(1.)
    go.z.append(-1.)
  go.x,go.y,go.z = np.array(go.x),np.array(go.y),np.array(go.z) # put arrays
  # now modify the hamiltonian
  ho = deepcopy(h)
  n = len(ho.intra) # dimension
  intra = [[0. for i in range(2*n)] for j in range(2*n)]
  inter = [[0. for i in range(2*n)] for j in range(2*n)]
  norb = n # number of orbitals
  # get the atoms which hop according to monolayer type...
  if h.has_spin: 
    norb = norb/2
    tl = [] # interlayer pairs
    x, y, z = go.x, go.y, go.z
    for i in range(len(x)): # loop over atoms
      for j in range(len(x)): # loop over atoms
        if 1.9 < np.abs(z[i]-z[j]) < 2.1: # if in contiguous layers 
          dd = (x[i]-x[j])**2 + (y[i] - y[j])**2 + (z[i] - z[j])**2
          if 3.9<dd<4.1:
            tl.append([i,j])
    for i in range(norb):
      for j in range(norb):  # assign interlayer hopping
        for s in range(2):
         for l in range(nlayers):
          intra[2*nlayers*i+s+2*l][2*nlayers*j+s+2*l] = h.intra[2*i+s,2*j+s]
          inter[2*nlayers*i+s+2*l][2*nlayers*j+s+2*l] = h.inter[2*i+s,2*j+s]
    # now put the interlayer hopping
    for p in tl:
      for s in range(2): # loop over spin
        intra[2*p[0]+s][2*p[1]+s] = t  
        intra[2*p[1]+s][2*p[0]+s] = np.conjugate(t)  
  else: raise # not implemented...
  if h.has_eh: raise # not implemented ....
  ho.intra = np.matrix(intra)
  ho.inter = np.matrix(inter)
  ho.geometry = go
  return ho   



def add_electric_field(h,e = 0.0):
  """Adds electric field to the system"""
  if h.has_spin: # if has spin
    z = h.geometry.z # z coordinates
    for i in range(len(h.intra)/2):
      h.intra[2*i,2*i] += z[i]*e 
      h.intra[2*i+1,2*i+1] += z[i]*e 
 





