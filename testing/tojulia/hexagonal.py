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


def bulk2ribbon(h,n=10):
  """Converts a hexagonal bulk hamiltonian into a ribbon hamiltonian"""
  h = honeycomb2square(h) # create a square 2d geometry
  go = h.geometry.copy() # copy geometry
  ho = h.copy() # copy hamiltonian
  ho.dimensionality = 1 # reduce dimensionality
  go.dimensionality = 1 # reduce dimensionality
  intra = [[None for i in range(n)] for j in range(n)]
  inter = [[None for i in range(n)] for j in range(n)]
  for i in range(n): # to the the sam index
    intra[i][i] = csc(h.intra) 
    inter[i][i] = csc(h.ty) 
  for i in range(n-1): # one more or less
    intra[i][i+1] = csc(h.tx)  
    intra[i+1][i] = csc(h.tx.H)  
    inter[i+1][i] = csc(h.txmy.H) 
    inter[i][i+1] = csc(h.txy) 
  ho.intra = bmat(intra).todense()
  ho.inter = bmat(inter).todense()
  return ho

