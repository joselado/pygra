import scipy.sparse.linalg as lg 
from scipy.sparse import csc_matrix as csc
import numpy as np


class pair_mf:
  """ Classs for mean field matrices"""
  def __init__(self,a,b,g=0.0):
    self.a = a # B matrix
    self.b = b # A matrix
    self.g = g # coupling


def hubbard(h,U=1.0,pairs = []):
  """ Creates mean field matrices for the input hamiltonian,
      returns list with mean field amtrix pairs in csc form"""
  hubm = [] # list with the hubbard mean field matrices
  if len(pairs)==0:
    de = len(h.intra) # dimension of the hamiltonian
    pairs = range(de/2) # create list with oribtal indices
  for i in pairs: # loop over up down pairs
    # density density term    
    data = [1.0+0.j] # value of the term in the matrix
    ij = [[2*i],[2*i]] # indexes in the matrix
    a = csc((data,ij),shape=(de,de))
    ij = [[2*i+1],[2*i+1]] # indexes in the matrix
    b = csc((data,ij),shape=(de,de))
    hubm += [pair_mf(a,b,g=U)] # add mean field pair
    # exchange exchange term    
    data = [1.0+0.j] # value of the term in the matrix
    ij = [[2*i],[2*i+1]] # indexes in the matrix
    a = csc((data,ij),shape=(de,de))
    ij = [[2*i+1],[2*i]] # indexes in the matrix
    b = csc((data,ij),shape=(de,de))
    hubm += [pair_mf(a,b,g= -U)] # add mean field pair
  return hubm # return list with the pairs


def selfconsistency(h,ab_list=None,nkp = 100,filling=0.5,old_mf=None):
  """ Solve a selfocnsistent mean field one dimensional system"""
  from scipy.linalg import eigh
  from operator import itemgetter
  if ab_list==None: ab_list=hubbard(h)
  intra = h.intra  # intramatrix
  inter = h.inter  # intermatrix
  if old_mf==None:  old_mf = intra*0.
  while True: # infinite loop
    htmp = h.copy()  # copy hamiltonian
    htmp.intra += old_mf # add mean field 
    eigvals,eigvecs = htmp.eigenvectors(nkp) # get eigenvectors
    # get the fermi energy
    ne = len(eigvals) ; ifermi = int(round(ne*filling))
    fermi = sorted(eigvals)[ifermi]
    mf = ab_list[0].a*0. # initialize mean field
    for (e,v) in zip(eigvals,eigvecs): # loop over eigenvals,eigenvecs
      for iab in ab_list: # loop over mean field matrices
        if e<fermi:  # if level is filled, add contribution
          a = iab.a # A matrix
          b = iab.b # B matrix
          g = iab.g # coupling
          vav = (v.H * a * v).todense()[0,0] # <vAv>
          vbv = (v.H * b * v).todense()[0,0] # <vBv>
          mf = mf + (vav*b + vbv*a)*g # mean field hamiltonian 
    mf = mf.todense() # new intramatrix
    if h.dimensionality>0: mf = mf/float(nkp) # normalize by nkvectors
    error = np.max(np.abs(old_mf-mf)) # absolute difference
    print "Error in SCF =",error
    old_mf = old_mf*0.1 + mf*0.9 # mixing
    if error<0.001: # if converged break
      break
  return mf # return mean field

def ferro_initialization(h,value = 0.1):
  mf = h.intra*0.0
  for i in range(len(mf)/2):
    mf[2*i,2*i] = value
    mf[2*i+1,2*i+1] = -value
  return mf



def antiferro_initialization(h,value = 0.1):
  mf = h.intra*0.0
  for i in range(len(mf)/2):
    v = value*(-1)**i
    mf[2*i,2*i] = v
    mf[2*i+1,2*i+1] = -v
  return mf




