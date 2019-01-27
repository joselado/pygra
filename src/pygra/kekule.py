import numpy as np
from . import geometry


remove_duplicated = geometry.remove_duplicated_positions

### Routines dealing with Kekule order ###

def kekule_positions(r):
    """
    Returns the positions defining a Kekule ordering
    """
    cs = hexagon_centers(r,r) # return the centers
    cs = remove_duplicated(cs) # remove duplicated
    cs = retain(cs,d=3.0) # retain only centers that are at distance 2
    return np.array(cs) # return array


def kekule_function(r,t=1.0):
    """
    Returns a function that will compute Kekule hoppings
    """
    cs = kekule_positions(r) # get the centers with all the positions
    ## Define a function to only have hoppings in the hexagon
    def f(r1,r2):
        for c in cs: # loop over centers
            dr = r1-r2 ; dr =dr.dot(dr) 
            if not 0.99<dr<1.01: continue
            dr1 = c-r1 ; dr1 = dr1.dot(dr1) # distance to r1
            dr2 = c-r2 ; dr2 = dr2.dot(dr2) # distance to r2
            if 0.99<dr1<1.01 and 0.99<dr2<1.01: # if clse to center
                return 1.0
        return 0.0 # no hopping
    # now define the function
    def fm(rs1,rs2):
      m = np.zeros((len(rs1),len(rs2)),dtype=np.complex) # initialize matrix
      for i in range(len(rs1)): # loop
        for j in range(len(rs2)): # loop
            m[i,j] = f(rs1[i],rs2[j]) # get kekule coupling
      return m*t # return the Kekule matrix
    return fm # return the function


def kekule_matrix(r1,r2=None):
    """
    Return a Kekule matrix for positions r, assuming
    they are from a honeycomb-like lattice
    """
    if r2 is None: r2 = r1
    f = kekule_function(r1)
    return f(r1,r2)


def hexagon_centers(r1,r2):
    """
    Return the centers of an hexagon
    """
    out = []
    for ri in r1: # loop
        for rj in r2: # loop
            dr = ri-rj
            dr = dr.dot(dr) # distance
            if 3.9<dr<4.1: # center of an hexagon
                out.append((ri+rj)/2.) # store the center
    return out # return list with centers


def r_in_rs(r,rs):
    """
    Check that a position is not stored
    """
    for ri in rs:
        dr = ri-r ; dr = dr.dot(dr)
        if dr<0.01: return True
    return False



def retain(r,d=3.0):
    """
    Retain only sites that are at a distance d
    """
    i = np.random.randint(len(r))
    out = [r[0]] # take first one
    def iterate(out): # do one iteration
      out0 = [r for r in out] # initialize
      for rj in out: # loop over stored
        for ri in r: # loop
            dr = ri-rj ; dr = dr.dot(dr) # distance
            if d*d-0.1<dr<d*d+0.1: # if desired distance
                # now check that this one has not been stored already
                if not r_in_rs(ri,out0): # not stored yet
                  out0.append(ri) # store position
      return out0
#    np.savetxt("R.OUT",np.matrix(r))
#    exit()
    while True:
#    for i in range(10):
        out1 = iterate(out) # do one iteration
        out1 = remove_duplicated(out1) # remove duplicated atoms
        if len(out1)==len(out): break
        out = [r for r in out1] # redefine
#    np.savetxt("R.OUT",np.matrix(out)) # write in file
#    exit()
    return out # return desired positions



