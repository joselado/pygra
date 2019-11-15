# function to work with spinless superconductivity
from numba import jit
from .. import algebra
import numpy as np

def onsite_delta_vev(h,nk=1,**kwargs):
    """Compute the expectation value of delta"""
    (es,ws) = h.get_eigenvectors(nk=nk,**kwargs) # compute the eigenvectors
    fac = 1./(nk**h.dimensionality) # number of kpoints
    wout = [] # empty list
    for i in range(len(es)):
        if es[i]<0.0: wout.append(ws[i]) # store
    wout = np.array(wout) # transform to array
    ni = h.intra.shape[0]//2 # number of sites
    p = np.zeros(ni,dtype=np.complex) # initialize
    p = compute_pairing(wout,p) # compute the pairing
    p = p*fac # normalize
    return p # return the pairing

@jit
def compute_pairing(ws,p):
    """Compute the pairing"""
    n = len(ws) # number of wavefunctions
    ni = len(ws[0])//2 # number of electron components
    for i in range(n): # loop over wavefunctions
        w = ws[i] # store
        for j in range(ni): # loop over components
            p[j] = p[j] + w[2*j]*np.conjugate(w[2*j+1]) # anomalous part
    return p # return expectation value



def swave_matrix(d):
    """Add swave pairing to a Hamiltonian, input is an array"""
    md = np.diag(d) # pairing matrix
    mdh = np.conjugate(md.T) # Hermitian
    m = algebra.bmat([[None,md],[mdh,None]]) # return matrix
    m = reorder(m) # reorder the entries
    return m


def add_swave_to_hamiltonian(h,d):
    """Add swave pairing to the hamiltonian"""
    if h.check_mode("spinless"):
      h.modify_hamiltonian_matrices(nambu) # modify the matrices
    elif h.check_mode("spinless_nambu"): pass # do nothing
    else: raise
    n = h.intra.shape[0]//2 # orbitals
    h.intra = h.intra + swave_matrix(np.ones(n)*d) # add matrix
    h.has_eh = True # has electron hole


def nambu(m):
    out = algebra.bmat([[m,None],[None,-np.conjugate(m)]])
    return reorder(out) # return matrix



def reorder(m):
  """Reorder a matrix that has electrons and holes"""
  R = np.array(np.zeros(m.shape)) # zero matrix
  nr = m.shape[0]//2 # number of positions
  for i in range(nr): # electrons
    R[i,2*i] = 1.0 # up electron
    R[i+nr,2*i+1] = 1.0 # down holes
  return R.T@m@R


def extract_swave(m):
    """Extract the swave vector form a matrix"""
    n = m.shape[0]//2 # number of orbitals
    out = np.zeros(n,dtype=np.complex) # initialize
    for i in range(n):
        out[i] = m[2*i,2*i+1]
    return out


def proje(n):
    """Return the projection operator in the electron sector"""
    m = np.zeros((n,n),dtype=np.complex)
    for i in range(n//2):
        m[2*i,2*i] = 1.0
    return m


