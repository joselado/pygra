# library to create operators
import numpy as np
from scipy.sparse import csc_matrix as csc

def interface1d(h,cut = 3.):
  dind = 1 # index to which divide the positions
  if h.has_spin:  dind *= 2 # duplicate for spin
  if h.has_eh:  dind *= 2  # duplicate for eh
  n = len(h.intra) # number of elments of the hamiltonian
  data = [] # epmty list
  for i in range(n): # loop over elements
    y = h.geometry.y[i/dind]
    if y < -cut:  data.append(-1.)
    elif y > cut: data.append(1.)
    else: data.append(0.)
  row, col = range(n),range(n)
  m = csc((data,(row,col)),shape=(n,n),dtype=np.complex)
  return m # return the operator

