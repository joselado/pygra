import invert
import numpy as np
from scipy.sparse import csc_matrix,bmat


# create the diagonals of a  
n = 5
d = [np.random.random((4,4)) for i in range(n)]   # diagonal
a = [np.random.random((4,4)) for i in range(n-1)]  # upper block
b = [np.random.random((4,4)) for i in range(n-1)]  # lower block


# build the matrix to invert by blocks
m = [[None for i in range(n)] for j in range(n)]
for i in range(n):
  m[i][i] = d[i]
for i in range(n-1):
  m[i][i+1] = a[i]
  m[i+1][i] = b[i]

mden = bmat(m).todense() # dense matrix

minv_usual = mden.I # inverse matrix with a usual algorithm

# list with block element of th inverse
minv = [[None for i in range(n)] for j in range(n)]

# Calculate inverse block by block with the testing algorithm 
for i in range(n):  # loop over rows
  for j in range(n):  # loop over columns
    # block i,j of the inverse
    minv[i][j] = csc_matrix(invert.gauss_inverse(d,a,b,i=i,j=j))
    # beware that python starts in 0!!!

# convert to dense matrix
minv = bmat(minv).todense()




print "Error between normal and block algorithm"
print np.max(np.abs(minv_usual - minv))


