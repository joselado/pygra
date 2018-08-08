import numpy as np
import scipy.sparse.linalg as lg


def current1d(h,nk=100,e=0.0,delta=0.01):
  """Calcualte the spatial profile of the current"""
  if h.dimensionality != 1: raise # only 1 dimensional
  hkgen = h.get_hk_gen() # get generator of the hamiltonian
  ks = np.linspace(0,1.,nk) # generate k points
  for k in ks: # loop over kpoints
    hk = hkgen(k) # get k-hamiltonian
    phik = np.exp(1j*2.*np.pi*k) # complex phase
    jk = 1j*(h.inter*phik - h.inter.H*np.conjugate(phik)) # current 
    evasl,evecs = lg.eigh(hk) # eigenvectors and eigenvalues
    evecs = np.transpose(evecs) # transpose eigenvectors
    



