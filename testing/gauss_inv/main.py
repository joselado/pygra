import green
import numpy as np
from scipy.sparse import csc_matrix,bmat

n = 5

def randm():
  return np.random.random((4,4)) + 1j*np.random.random((4,4))


d = [randm() for i in range(n)]
a = [randm() for i in range(n-1)]
b = [randm() for i in range(n-1)]


m = [[None for i in range(n)] for j in range(n)]
for i in range(n):
  m[i][i] = d[i]
for i in range(n-1):
  m[i][i+1] = a[i]
  m[i+1][i] = b[i]

mden = bmat(m).todense() # dense matrix

minv = [[None for i in range(n)] for j in range(n)]

for i in range(n):
  for j in range(n):
    minv[i][j] = csc_matrix(green.gauss_inverse(m,i=i,j=j))

minv = bmat(minv).todense()

print "Maximun error"
print np.max(np.abs(mden.I - minv))


