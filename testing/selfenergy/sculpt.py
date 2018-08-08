import geometry
from copy import deepcopy
import numpy as np


def remove(g,l):
  """ Remove certain atoms from the geometry"""
  nr = len(l) # number of removed atoms
  go = deepcopy(g) # copy the list
  xo = [] # copy the list
  yo = [] # copy the list
  for i in range(len(g.x)):
    if not i in l:
      xo.append(g.x[i])
      yo.append(g.y[i])
  go.x = np.array(xo)
  go.y = np.array(yo)
  return go

def intersec(g,f):
  """ Intersec coordinates with a certain function which yields True or False,
  output is resultant geometry """
  gout = deepcopy(g) # copy the geometry
  x = [] # out x
  y = [] # out y
  for (ix,iy) in zip(g.x,g.y): # loop over positions
    if f(ix,iy): # if the function yields true
      x.append(ix)
      y.append(iy)
  gout.x = np.array(x)  # copy x
  gout.y = np.array(y)  # copy y
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
  phi = np.pi*angle # angle in radians
  go = deepcopy(g)
  go.x = np.array([np.cos(phi)*g.x[i] + np.sin(phi)*g.y[i]] for i in range(len(g.x)))  
  go.y = np.array([-np.sin(phi)*g.x[i] + np.cos(phi)*g.y[i]] for i in range(len(g.x)))  
  return go


def center(g,angle):
  """Center a geometry"""
  g.x = g.x -sum(g.x)/len(g.x)
  g.y = g.y -sum(g.y)/len(g.y)
 






