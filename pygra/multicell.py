import numpy as np

class Hopping(): pass


def turn_multicell(h):
  """Transform a normal hamiltonian into a multicell hamiltonian"""
  ho = h.copy() # copy hamiltonian
  if h.dimensionality != 2: raise # not implemented
  hoppings = [] # list of hoppings
  # directions
  dirs = []
  dirs.append(np.array([1.,0.,0.]))
  dirs.append(np.array([0.,1.,0.]))
  dirs.append(np.array([1.,1.,0.]))
  dirs.append(np.array([1.,-1.,0.]))
  ts = [h.tx,h.ty,h.txy,h.txmy]
  hoppings = []
  for (d,t) in zip(dirs,ts): # loop over hoppings
    hopping = Hopping() # create object
    hopping.m = t
    hopping.dir = d
    hoppings.append(hopping) # store
    hopping = Hopping() # create object
    hopping.m = t.H
    hopping.dir = -d
    hoppings.append(hopping) # store
  ho.hopping = hoppings # store all the hoppings
  ho.is_multicell = True # multicell hamiltonian
  return ho


def get_tij(h,rij=np.array([0.,0.,0.])):
  """Get the hopping between cells with certain indexes"""
  drij = [int(round(ir)) for ir in rij] # put as integer
  drij = (drij[0],drij[1],drij[2]) # as a tuple
  try: return h.hopping_dict[drij] # try using the dictionary
  except: # if it doesn't exist, look for it
    rij = np.array(rij) # convert into array
    if rij.dot(rij)<0.001: return h.intra # if vector 0
    for t in h.hopping: # loop over hoppings 
      d = t.dir - rij # diference vector
      d = d.dot(d) # module
      if d < 0.001: # if same vector
        h.hopping_dict[drij] = t.m # store element in dictionary
        return t.m # return matrix
    h.hopping_dict[drij] = None # store element in dictionary
    return None # not found

def hk_gen(h):
  """Generate a k dependent hamiltonian"""
  if h.is_multicell==False: raise
  if h.dimensionality == 0: return None
  if h.dimensionality == 1: # one dimensional
    def hk(k):
      """k dependent hamiltonian, k goes from 0 to 1"""
      mout = h.intra # intracell term
      for t in h.hopping: # loop over matrices
        phi = t.dir[0]*k # phase
        tk = t.m * np.exp(1j*np.pi*2.*phi) # k hopping
        mout = mout + tk 
      return mout
    return hk  # return the function
  if h.dimensionality == 2: # two dimensional
    def hk(k):
      """k dependent hamiltonian, k goes from 0 to 1"""
      k = np.array([k[0],k[1]]) # convert to array
      mout = h.intra # intracell term
      for t in h.hopping: # loop over matrices
        d = t.dir
        d = np.array([d[0],d[1]]) # vector director of hopping
        phi = d.dot(k) # phase
        tk = t.m * np.exp(1j*np.pi*2.*phi) # k hopping
        mout = mout + tk 
      return mout
    return hk  # return the function

def turn_spinful(h):
  """Turn a hamiltonian spinful"""
  from increase_hilbert import spinful
  if h.has_eh: raise
  if h.has_spin: return # return if already has spin
  h.has_spin = True # put spin
  h.intra = spinful(h.intra) # spinful intra
  for i in range(len(h.hopping)): 
    h.hopping[i].m = spinful(h.hopping[i].m) # spinful hopping

