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
  kp = np.linspace(0.,1.0,nkp) # list with kpoints
  if old_mf==None:  old_mf = intra*0.
  den_goal = filling * len(intra) * nkp # density goal
  while True: # infinite loop
    intra_mf = intra + old_mf # initialice mean field intramatrix
    eigvecs = [] # empty list with eigenvectors
    eigvals = [] # empty list with eigenvectors
    for k in kp: # loop over kpoints
      kphase = np.exp(2*np.pi*k*1j) # k phase
      tk = inter*kphase
      hk = intra_mf + tk + tk.H
      vv = eigh(hk) # diagonalize k hamiltonian
      eigvals += vv[0].tolist() # store eigenvalues
      vecs = [csc(np.matrix(v).T) for v in vv[1].transpose()]
      eigvecs += vecs # store eigenvectors in sparse form
    # sort eigenvalues and eigenvectors
    eigv = sorted(zip(eigvals,eigvecs),key=itemgetter(0))
    acc_den = 0.0 # acumulated density
    # add contribution until filling reached
    mf = ab_list[0].a*0. # initialize mean field
    for ieigv in eigv: # loop over eigenvals,eigenvecs
      v = ieigv[1] # eigenvectors (in csc matrix form)
      for iab in ab_list: # loop over mean field matrices
        a = iab.a # A matrix
        b = iab.b # B matrix
        g = iab.g # coupling
        vav = (v.H * a * v).todense()[0,0] # <vAv>
        vbv = (v.H * b * v).todense()[0,0] # <vBv>
        mf = mf + (vav*b + vav*a)*g 
      acc_den += (v.H *v).todense()[0,0] # add norm        
      if acc_den >= den_goal: # break if #e reached
        break
    mf = mf.todense()/float(nkp) # new intramatrix
    error = np.max(np.abs(old_mf-mf)) # absolute difference
    print "Error =",error,mf.shape
    old_mf = old_mf*0.1 + mf*0.9 # mixing
#    old_mf = mf # mixing
    if error<0.001: # if converged break
      break
  return mf # return mean field

def ferro_initialization(h,value = 0.1):
  mf = h.intra*0.0
  for i in range(len(mf)/2):
    mf[2*i,2*i] = value
    mf[2*i+1,2*i+1] = -value
  return mf

