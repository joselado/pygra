from copy import deepcopy
from scipy.sparse import bmat
from scipy.sparse import csc_matrix as csc
import numpy as np

def honeycomb2square(h):
  """Transforms a honeycomb lattice into a square lattice"""
  ho = deepcopy(h) # output geometry
  g = h.geometry # geometry
  go = deepcopy(g) # output geometry
  go.a1 = - g.a1 - g.a2 
  go.a2 = g.a1 - g.a2
  go.x = np.concatenate([g.x,g.x-g.a1[0]])
  go.y = np.concatenate([g.y,g.y-g.a1[1]])
  go.z = np.concatenate([g.z,g.z])
  zero = csc(h.tx*0.)
  # define sparse
  intra = csc(h.intra)
  tx = csc(h.tx)
  ty = csc(h.ty)
  txy = csc(h.txy)
  txmy = csc(h.txmy)
  # define new hoppings
  ho.intra = bmat([[intra,tx.H],[tx,intra]]).todense()
  ho.tx = bmat([[txy.H,zero],[ty.H,txy.H]]).todense()
  ho.ty = bmat([[txmy,ty.H],[txmy,zero]]).todense()
  ho.txy = bmat([[zero,None],[None,zero]]).todense()
  ho.txmy = bmat([[zero,None],[tx.H,zero]]).todense()
  ho.geometry = go
  return ho
