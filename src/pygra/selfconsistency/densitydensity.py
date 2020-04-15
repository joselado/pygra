# specialized routine to perform an SCF, taking as starting point an
# attractive local interaction in a spinless Hamiltonian

from .. import inout
import numpy as np
import time
import os
from .. import densitymatrix
from copy import deepcopy
from numba import jit

class Interaction():
    def __init__(self,h=None):
        self.dimensionality = 0
        if h is not None: self.dimensionality = h.dimensionality
        self.v_dict = dict() # store dictionary
    def __mult__(self,a):
        """Function to multiply"""
        out = 0
        for key in self: out = out + self[key]*a[key]
        return out



def normal_term(v,dm):
    """Return the normal term of the mean field"""
    out = dm*0.0 # initialize
    return normal_term_jit(v,dm,out) # return the normal term



def normal_term_ii(v,dm):
    """Return the normal term of the mean field"""
    out = dm*0.0 # initialize
    return normal_term_ii_jit(v,dm,out) # return the normal term


def normal_term_jj(v,dm):
    """Return the normal term of the mean field"""
    out = dm*0.0 # initialize
    return normal_term_jj_jit(v,dm,out) # return the normal term


def normal_term_ij(v,dm):
    """Return the normal term of the mean field"""
    out = dm*0.0 # initialize
    return normal_term_ij_jit(v,dm,out) # return the normal term


def normal_term_ji(v,dm):
    """Return the normal term of the mean field"""
    out = dm*0.0 # initialize
    return normal_term_ji_jit(v,dm,out) # return the normal term

@jit
def normal_term_jit(v,dm,out):
    """Return the normal terms, jit function"""
    n = len(v[0])
    for i in range(n): # loop
      for j in range(n): # loop
        out[i,j] = out[i,j] - v[i,j]*dm[j,i]
        out[j,i] = out[j,i] - v[i,j]*dm[i,j]
        out[i,i] = out[i,i] + v[i,j]*dm[j,j]
        out[j,j] = out[j,j] + v[i,j]*dm[i,i]
    return out


@jit
def normal_term_ii_jit(v,dm,out):
    """Return the normal terms, jit function"""
    n = len(v[0])
    for i in range(n): # loop
      for j in range(n): # loop
        out[i,i] = out[i,i] + v[i,j]*dm[j,j]
    return out

@jit
def normal_term_jj_jit(v,dm,out):
    """Return the normal terms, jit function"""
    n = len(v[0])
    for i in range(n): # loop
      for j in range(n): # loop
        out[j,j] = out[j,j] + v[i,j]*dm[i,i]
    return out


@jit
def normal_term_ij_jit(v,dm,out):
    """Return the normal terms, jit function"""
    n = len(v[0])
    for i in range(n): # loop
      for j in range(n): # loop
        out[i,j] = out[i,j] - v[i,j]*dm[j,i]
    return out


@jit
def normal_term_ji_jit(v,dm,out):
    """Return the normal terms, jit function"""
    n = len(v[0])
    for i in range(n): # loop
      for j in range(n): # loop
        out[j,i] = out[j,i] - v[i,j]*dm[i,j]
    return out



def update_hamiltonian(tdict,mf):
    """Update the hoppings with the mean field"""
    out = dict() # initialize
    for key in mf:
        out[key] = tdict[key] + mf[key] # add contribution
    return out # return dictionary


def mix_mf(mf,mf0,mix=0.8):
    """Mix mean fields"""
    out = dict() # initialize
    for key in mf: # loop
        out[key] = mf0[key]*(1.-mix) + mf[key]*mix # add contribution
    return out



def diff_mf(mf0,mf):
    """Difference mean fields"""
    out = 0.0 # initialize
    for key in mf: # loop
        out += np.mean(np.abs(mf0[key] - mf[key])) # add contribution
    return out # return


def hamiltonian2dict(h):
    out = dict() # create dictionary
    if not h.is_multicell: raise
    out[(0,0,0)] = h.intra
    for t in h.hopping: out[tuple(t.dir)] = t.m # store
    return out


def set_hoppings(h,hop):
    """Add the hoppings to the Hamiltonian"""
    h.is_multicell = True
    class Hop: pass
    h.intra = h.intra*0.0 # set to zero
    hopping = [] # empty list
    for key in hop: # loop
        t = Hop() # generate
        t.dir = np.array(key) # transform to array
        t.m = hop[key] # matrix
        hopping.append(t) # store
    h.hopping = hopping # store

def get_dm(h,nk=1):
    """Get the density matrix"""
    ds = [(0,0,0)] # directions
    if h.dimensionality>0:
      for t in h.hopping: ds.append(tuple(t.dir)) # store
    dms = densitymatrix.full_dm(h,ds=ds,nk=nk) # get all the density matrices
    dm = dict()
    for i in range(len(ds)): 
        dm[ds[i]] = dms[i] # store
    return dm # return dictionary with the density matrix

def get_mf(v,dm):
    """Get the mean field"""
    zero = dm[(0,0,0)]*0. # zero
    mf = dict()
    for d in v: mf[d] = zero.copy()  # initialize
    # compute the contribution to the mean field
    # onsite term
#    mf[(0,0,0)] = normal_term(v[(0,0,0)],dm[(0,0,0)]) 
    def dag(m): return m.T.conjugate()
    for d in v: # loop over directions
        d2 = (-d[0],-d[1],-d[2]) # minus this direction
        # add the normal terms
        m = normal_term_ij(v[d],dm[d2]) # get matrix
        mf[d] = mf[d] + m # add normal term
        mf[d2] = mf[d2] + dag(m) # add the normal terms
    return mf


mf_file = "MF.pkl" 

def densitydensity(h0,mf=None,mix=0.9,v=None,nk=8,solver="plain",
        maxerror=1e-5,filling=None,callback_mf=None,**kwargs):
    """Perform the SCF mean field"""
    h0.turn_dense()
#    if not h0.check_mode("spinless"): raise # sanity check
    h = h0.copy() # initial Hamiltonian
    if mf is None:
      try: mf = inout.load(mf_file) # load the file
      except: 
          mf = dict()
          for d in v: mf[d] = np.random.random(h.intra.shape) 
    else: pass # initial guess
    ii = 0
    os.system("rm -f STOP") # remove stop file
    hop0 = hamiltonian2dict(h) # create dictionary
    def f(mf):
      """Function to minimize"""
#      print("Iteration #",ii) # Iteration
      if os.path.exists("STOP"): return mf # return result
      hop = update_hamiltonian(hop0,mf) # add the mean field to the Hamiltonian
      set_hoppings(h,hop) # set the new hoppings in the Hamiltonian
      t0 = time.clock() # time
      dm = get_dm(h,nk=nk) # get the density matrix
      t1 = time.clock() # time
      mf = get_mf(v,dm) # return the mean field
      if callback_mf is not None:
          mf = callback_mf(mf)
      t2 = time.clock() # time
      print("Time in density matrix = ",t1-t0) # Difference
      print("Time in the normal term = ",t2-t1) # Difference
      return mf
    if solver=="plain":
      do_scf = True
      while do_scf:
        mfnew = f(mf) # new vector
        t0 = time.clock() # time
        diff = diff_mf(mfnew,mf) # mix mean field
        mf = mix_mf(mfnew,mf,mix=mix) # mix mean field
        t1 = time.clock() # time
        print("Time in mixing",t1-t0)
        print("ERROR",diff)
        print()
        if diff<maxerror: 
          do_scf = False
    else:
        print("Solver used:",solver)
        import scipy.optimize as optimize 
        if solver=="newton": fsolver = optimize.newton_krylov
        elif solver=="anderson": fsolver = optimize.anderson
        elif solver=="broyden": fsolver = optimize.broyden2
        elif solver=="linear": fsolver = optimize.linearmixing
        else: raise
        def fsol(x): return x - f(x) # function to solve
        dold = fsolver(fsol,dold,f_tol=maxerror)
    scf = SCF() # create object
    h = h0.copy() # copy Hamiltonian
    set_hoppings(h,mf) # set the new hoppings in the Hamiltonian
    h.intra = mf[(0,0,0)] # set the intra-term
    inout.save(mf,mf_file) # save the mean field
    scf.hamiltonian = h # store
    scf.mf = mf # store mean field
    return scf # return SCF object



class SCF(): pass

