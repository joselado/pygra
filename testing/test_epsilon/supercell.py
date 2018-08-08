

def intra_super2d(h,n=1,central=None):
  """ Calculates the intra of a 2d system"""
  from scipy.sparse import bmat
  from scipy.sparse import csc_matrix as csc
  tx = csc(h.tx)
  ty = csc(h.ty)
  txy = csc(h.txy)
  txmy = csc(h.txmy)
  intra = csc(h.intra)
  for i in range(n):
    intrasuper[i][i] = intra # intracell
    (x1,y1) = inds[i]
    for j in range(n):
      (x2,y2) = inds[j]
      dx = x2-x1
      dy = y2-y1
      if dx==1 and  dy==0: intrasuper[i][j] = tx
      if dx==-1 and dy==0: intrasuper[i][j] = tx.H
      if dx==0 and  dy==1: intrasuper[i][j] = ty
      if dx==0 and  dy==-1: intrasuper[i][j] = ty.H
      if dx==1 and  dy==1: intrasuper[i][j] = txy
      if dx==-1 and dy==-1: intrasuper[i][j] = txy.H
      if dx==1 and  dy==-1: intrasuper[i][j] = txmy
      if dx==-1 and dy==1: intrasuper[i][j] = txmy.H
  # substitute the central cell if it is the case
  if central!=None:
    ic = (n-1)/2
    intrasuper[ic][ic] = central
  # now convert to matrix
  intrasuper = bmat(intrasuper).todense() # supercell
  return intrasuper


