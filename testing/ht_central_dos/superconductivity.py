from __future__ import print_function
import numpy as np



def get_eh_sector_odd_even(m,i=0,j=0):
  """ Return the electron hole sector of a matrix, 
  assuming the form is even index for electrons and odd for holes"""
  if i>1 or j>1: raise # meaningless
  n = m.shape[0]//2 # size of the matrix 
  mout = np.matrix(np.zeros((n,n)),dtype=np.complex) # define matrix
  for ii in range(n): # loop over index
    for jj in range(n): # loop over index
      mout[ii,jj] = m[2*ii+i,2*jj+j] # assign
  return mout # return matrix



def get_nambu_tauz(m,has_eh=False):
  """Return the nambu matrix tauz for electron-hole"""
  n = m.shape[0] # number of sites 
  if has_eh: n = n//2 # half
  mout = np.matrix(np.zeros((n*2,n*2)),dtype=np.complex) # define matrix
  for ii in range(n): # loop over index
    mout[2*ii,2*ii] = 1. # assign
    mout[2*ii+1,2*ii+1] = -1. # assign
  return mout # return tauz



def project_electrons(m):
  """Return the nambu matrix tauz for electron-hole"""
  n = m.shape[0] # number of sites 
  mout = m*0.0 # define matrix
  for ii in range(n): # loop over index
    for jj in range(n): # loop over index
      if ii%2==0 and jj%2==0:  mout[ii,jj] = m[ii,jj] # assign
      else: continue
  return mout # return tauz



def project_holes(m):
  """Return the nambu matrix tauz for electron-hole"""
  n = m.shape[0] # number of sites 
  mout = m*0.0 # define matrix
  for ii in range(n): # loop over index
    for jj in range(n): # loop over index
      if ii%2==1 and jj%2==1:  mout[ii,jj] = m[ii,jj] # assign
      else: continue
  return mout # return tauz


def build_eh(hin,coupling=None):
  """Creates a electron hole matrix, from an input matrix, coupling couples
     electrons and holes
      - hin is the hamiltonian for electrons, which has the usual common form
      - coupling is the matrix which tells the coupling between electron
        on state i woth holes on state j, for exmaple, with swave pairing
        the non vanishing elments are (0,1),(2,3),(4,5) and so on..."""
  n = len(hin)  # dimension of input
  nn = 2*n  # dimension of output
  hout = np.matrix(np.zeros((nn,nn),dtype=complex))  # output hamiltonian
  for i in range(n):
    for j in range(n):
      hout[2*i,2*j] = hin[i,j]  # electron term
      hout[2*i+1,2*j+1] = -np.conjugate(hin[i,j])  # hole term
  if not coupling is None: # if there is coupling
    for i in range(n):
      for j in range(n):
        # couples electron in i with hole in j
        hout[2*i,2*j+1] = coupling[i,j]  # electron hole term
        # couples hole in i with electron in j
        hout[2*j+1,2*i] = np.conjugate(coupling[i,j])  # hole electron term
  return hout





