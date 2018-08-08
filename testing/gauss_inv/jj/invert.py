import numpy as np

def gauss_inverse(d,a,b,i=0,j=0):
  from gauss_inv import gauss_inv as ginv
  """ Calculates the block element of the inverse a block diagonal
      matrix, d are diagonal blocks and a,b the upper and lower diagonals """
  if not len(d)==len(a)+1==len(b)+1:
    print "Wrong dimensions of diagonals"
    raise
  mout = ginv(d,b,a,i+1,j+1)  # call the fortran function
  return np.matrix(mout)
