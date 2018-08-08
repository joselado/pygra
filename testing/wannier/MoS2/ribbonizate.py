import numpy as np

def bulk2ribbon(g, n=5):
  """ Transformas a 2D geometry into a ribbon"""
  if not g.dimensionality == 2: raise # has to be two dimensional
  if not np.abs(g.a1.dot(g.a2)) < 0.0001: raise # has to be orthogonal
  go = g.copy() # create new geometry
  go.dimensionality = 1 # ribbon
  go.x = []
  go.y = []
  go.z = []
  for i in range(n):
    go.x += (g.x).tolist() # append x
    go.z += (g.z).tolist() # append x
    go.y += (g.y+i*g.a2[1]).tolist() # append x
  go.x = np.array(go.x)
  go.y = np.array(go.y)
  go.z = np.array(go.z)
  go.xyz2r()
  go.celldis = g.a1[0]
  go.center()
  return go


def reflect(g):
  """ Reflcts a certain geometry with respect to the origin"""
  g.y = g.y - min(g.y) # move to the zero
  go = g.copy()
  go.x = (g.x).tolist() + (g.x).tolist()
  go.y = (g.y).tolist() + (-g.y).tolist()
  go.z = (g.z).tolist() + (g.z).tolist()
  go.x = np.array(go.x)
  go.y = np.array(go.y)
  go.z = np.array(go.z)
  go.xyz2r()
  go = remove_repeated(go) # remove the repeted atoms
  return go  




def remove_repeated(g):
  """ Remove repeated coordinates"""
  go = g.copy() # copy geometry
  go.r = [] # empty list
  for i in range(len(g.r)): # only accept
    unique = True
    for j in range(len(go.r)):
      if i!=j:
        dr = g.r[i] -g.r[j]
        dr = dr.dot(dr) # distance
        if dr<0.2:
          unique=False
    if unique:
      go.r.append(g.r[i])
    else:
      print "Repeated",i
  go.r = np.array(go.r)
  go.r2xyz()
  return go


 


