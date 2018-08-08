# routines to extract channels from a matrix
from __future__ import division
import numpy as np

def spin_channel(m,spin_column=None,spin_row=None,has_spin=True):
  """Extract a channel from a matrix"""
  if not has_spin: return m # return initial
  if (spin_row is None) or (spin_column is None): return m # return initial
  n = m.shape[0] # shape of the matrix
  n2 = n//2 # number of orbitals
  out = np.zeros((n,n),dtype=np.complex)
  if spin_column=="up": ii = 0
  else: ii = 1
  if spin_row=="up": jj = 0
  else: jj = 1
  for i in range(n2):
    for j in range(n2): out[i,j] = m[2*i+ii,2*j+jj]
  return np.matrix(out)

