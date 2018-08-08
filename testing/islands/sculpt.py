import geometry
from copy import deepcopy
import numpy as np


def remove(g,l):
  """ Remove certain atoms from the geometry"""
  nr = len(l) # number of removed atoms
  go = g.copy() # copy the geometry
  xo = [] # copy the list
  yo = [] # copy the list
  zo = [] # copy the list
  for i in range(len(g.x)):
    if not i in l:
      xo.append(g.x[i])
      yo.append(g.y[i])
      zo.append(g.z[i])
  go.x = np.array(xo)
  go.y = np.array(yo)
  go.z = np.array(zo)
  go.xyz2r() # update the revectors
  return go

def intersec(g,f):
  """ Intersec coordinates with a certain function which yields True or False,
  output is resultant geometry """
  gout = g.copy() # copy the geometry
  x = [] # out x
  y = [] # out y
  z = [] # out y
  for (ix,iy,iz) in zip(g.x,g.y,g.z): # loop over positions
    if f(ix,iy): # if the function yields true
      x.append(ix)
      y.append(iy)
      z.append(iz)
  gout.x = np.array(x)  # copy x
  gout.y = np.array(y)  # copy y
  gout.z = np.array(z)  # copy y
  gout.xyz2r() # update r
  return gout


def circle(r=1.0,out=False):
  """ Returns a function which encondes a circle"""
  if out:  # if true is inside
    def f(x,y):
      if r*r > x*x + y*y:
        return True
      else:
        return False  
  else: # if true is outside
    def f(x,y):
      if r*r < x*x + y*y:
        return True
      else:
        return False  
  return f # return the function



def rotate(g,angle):
  """ Rotates a geometry"""
#  phi = np.pi*angle # angle in radians
  phi = angle
  go = g.copy()
  # modify x and y, z is the same
  x,y,z = [],[],[]  # initialize lists
  c,s = np.cos(phi), np.sin(phi)  # sin and cos of the anggle
  for (ix,iy,iz) in zip(g.x,g.y,g.z):
    x.append(c*ix + s*iy)    # x coordinate 
    y.append(-s*ix + c*iy)    # y coordinate
    z.append(iz)
  go.x = np.array(x)
  go.y = np.array(y)
  go.z = np.array(z)
  go.xyz2r() # update r
  return go


def center(g,angle):
  """Center a geometry"""
  g.x = g.x -sum(g.x)/len(g.x)
  g.y = g.y -sum(g.y)/len(g.y)
 


def remove_unibonded(g,d=1.0,tol=0.1):
  """Removes from the geometry atoms with only one bond"""
  sb = []
  for i in range(len(g.r)): 
    r1 = g.r[i] # first position
    nb = 0 # initialize
    for r2 in g.r:
      dr = r1-r2
      if d-tol < dr.dot(dr) < d+tol: # if sirdt neighbor
        nb += 1 # increase counter
    if nb==1:
      sb.append(i+0) # add to the list
  return remove(g,sb) # remove those atoms



