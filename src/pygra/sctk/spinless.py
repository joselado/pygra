# function to work with spinless superconductivity
from numba import jit
from .. import algebra
import numpy as np

def onsite_delta_vev(h,nk=1,**kwargs):
    """Compute the expectation value of delta"""
    (es,ws) = h0.get_eigenvectors(nk=nk) # compute the eigenvectors
    nk = len(ws)/h.intra.shape[0] # number of kpoints
    wout = [] # empty list
    for i in range(len(es)):
        if e<0.0: wout.append(w) # store
    wout = np.array(wout) # transform to array
    ni = h.intra.shape[0]//2 # number of sites
    p = np.zeros(ni,dtype=np.complex) # initialize
    p = compute_pairing(wout,p) # compute the pairing
    p = p/nk # normalize
    return p # return the pairing


@jit
def compute_pairing(ws,p):
    """Compute the pairing"""
    n = len(ws) # number of wavefunctions
    ni = len(ws) # number of electron components
    for i in range(n): # loop over wavefunctions
        w = ws[i] # store
        for j in range(ni): # loop over components
            p[j] = p[j] + w[2*j]*w[2*j+1] # anomalous part
    return p # return expectation value



def add_swave(m,d):
    """Add swave pairing to a Hamiltonian, input is an array"""
    if m.shape[0]!=len(d): raise
    md = np.diag(d,dtype=np.complex) # pairing matrix
    mdh = np.conjugate(md.T)
    m = algebra.bmat([[m,md],[mdh,-m]]) # return matrix
    return m

