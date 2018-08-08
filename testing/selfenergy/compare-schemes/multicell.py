import numpy as np
from scipy.sparse import csc_matrix,bmat


class Hopping(): pass


def turn_multicell(h):
  """Transform a normal hamiltonian into a multicell hamiltonian"""
  ho = h.copy() # copy hamiltonian
  if ho.is_multicell: return ho # if it is already multicell
  if h.dimensionality != 2: raise # not implemented
  hoppings = [] # list of hoppings
  # directions
  dirs = []
  dirs.append(np.array([1,0,0]))
  dirs.append(np.array([0,1,0]))
  dirs.append(np.array([1,1,0]))
  dirs.append(np.array([1,-1,0]))
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


def get_tij(h,rij=np.array([0.,0.,0.]),zero=False):
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
  elif h.dimensionality == 1: # one dimensional
    def hk(k):
      """k dependent hamiltonian, k goes from 0 to 1"""
      mout = h.intra # intracell term
      for t in h.hopping: # loop over matrices
        phi = t.dir[0]*k # phase
        tk = t.m * np.exp(1j*np.pi*2.*phi) # k hopping
        mout = mout + tk 
      return mout
    return hk  # return the function
  elif h.dimensionality == 2: # two dimensional
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
  elif h.dimensionality == 3: # three dimensional
    def hk(k):
      """k dependent hamiltonian, k goes from 0 to 1"""
      k = np.array([k[0],k[1],k[2]]) # convert to array
      mout = h.intra # intracell term
      for t in h.hopping: # loop over matrices
        d = t.dir
        d = np.array([d[0],d[1],d[2]]) # vector director of hopping
        phi = d.dot(k) # phase
        tk = t.m * np.exp(1j*np.pi*2.*phi) # k hopping
        mout = mout + tk 
      return mout
    return hk  # return the function
  else: raise







def turn_spinful(h):
  """Turn a hamiltonian spinful"""
  from increase_hilbert import spinful
  if h.has_eh: raise
  if h.has_spin: return # return if already has spin
  h.has_spin = True # put spin
  h.intra = spinful(h.intra) # spinful intra
  for i in range(len(h.hopping)): 
    h.hopping[i].m = spinful(h.hopping[i].m) # spinful hopping




def bulk2ribbon(hin,n=10,sparse=True,nxt=6,ncut=6):
  """ Create a ribbon hamiltonian object"""
  if not hin.is_multicell: h = turn_multicell(hin)
  else: h = hin # nothing othrwise
  hr = h.copy() # copy hamiltonian
  if sparse: hr.is_sparse = True # sparse output
  hr.dimensionality = 1 # reduce dimensionality
  # stuff about geometry
  hr.geometry = h.geometry.supercell((1,n)) # create supercell
  hr.geometry.dimensionality = 1
  hr.geometry.a1 = h.geometry.a1 # add the unit cell vector
  import sculpt # rotate the geometry
  hr.geometry = sculpt.rotate_a2b(hr.geometry,hr.geometry.a1,np.array([1.,0.,0.]))
  hr.geometry.celldis = hr.geometry.a1[0]

  def superhopping(dr=[0,0,0]): 
    """ Return a matrix with the hopping of the supercell"""
    intra = [[None for i in range(n)] for j in range(n)] # intracell term
    for ii in range(n): # loop over ii
      for jj in range(n): # loop over jj
        d = np.array([dr[0],ii-jj+dr[1],dr[2]])
        if d.dot(d)>ncut*ncut: continue # skip iteration
        m = get_tij(h,rij=d) # get the matrix
        if m is not None: intra[ii][jj] = csc_matrix(m) # store
        else: 
          if ii==jj: intra[ii][jj] = csc_matrix(h.intra*0.)
    intra = bmat(intra) # convert to matrix
    if not sparse: intra = intra.todense() # dense matrix
    return intra
  # get the intra matrix
  hr.intra = superhopping()
  # now do the same for the interterm
  hoppings = [] # list of hopings
  for i in range(-nxt,nxt+1): # loop over hoppings
    if i==0: continue # skip the 0
    d = np.array([i,0.,0.])
    hopp = Hopping() # create object
    hopp.m = superhopping(dr=d) # get hopping of the supercell
    hopp.dir = d
    hoppings.append(hopp)
  hr.hopping = hoppings # store the list
  return hr 




def rotate(h):
  """ Rotate 90 degrees the Hamiltonian"""
#  raise
  ho = turn_multicell(h) # copy Hamiltonian
  hoppings = []
  for i in range(len(ho.hopping)):
    tdir = ho.hopping[i].dir 
    ho.hopping[i].dir = np.array([tdir[1],tdir[0],tdir[2]]) # new direction
  ho.geometry.a1,ho.geometry.a2 = h.geometry.a2,h.geometry.a1
  return ho



def clean(h,cutoff=0.0001):
  """Remove hoppings smaller than a certain quantity"""
  ho = h.copy() # copy hamiltonian
  raise 



def supercell(hin,nsuper=[1,1,1],sparse=True,ncut=3):
  """ Create a ribbon hamiltonian object"""
  if not hin.is_multicell: h = turn_multicell(hin)
  else: h = hin # nothing othrwise
  hr = h.copy() # copy hamiltonian
  if sparse: hr.is_sparse = True # sparse output
  # stuff about geometry
  hr.geometry = h.geometry.supercell(nsuper) # create supercell
  n = nsuper[0]*nsuper[1]*nsuper[2] # number of cells in the supercell
  pos = [] # positions inside the supercell
  for i in range(nsuper[0]):
    for j in range(nsuper[1]):
      for k in range(nsuper[2]):
        pos.append(np.array([i,j,k])) # store position inside the supercell
  zero = h.intra*0. # zero matrix
  def superhopping(dr=[0,0,0]): 
    """ Return a matrix with the hopping of the supercell"""
    rs = [dr[0]*nsuper[0],dr[1]*nsuper[1],dr[2]*nsuper[2]] # supercell vector
    intra = [[None for i in range(n)] for j in range(n)] # intracell term
    for ii in range(n): # loop over cells
      for jj in range(n): # loop over cells
        d = pos[jj] + np.array(rs) -pos[ii] # distance
      #  if d.dot(d)>ncut*ncut: continue # skip iteration
        m = get_tij(h,rij=d) # get the matrix
        if m is not None: intra[ii][jj] = csc_matrix(m) # store
        else: 
          intra[ii][jj] = csc_matrix(zero)
    intra = bmat(intra) # convert to matrix
    if not sparse: intra = intra.todense() # dense matrix
    return intra
  # get the intra matrix
  hr.intra = superhopping()
  # now do the same for the interterm
  hoppings = [] # list of hopings
  for i in range(-ncut,ncut+1): # loop over hoppings
    for j in range(-ncut,ncut+1): # loop over hoppings
      for k in range(-ncut,ncut+1): # loop over hoppings
        if i==j==k==0: continue # skip the intraterm
        dr = np.array([i,j,k])
        hopp = Hopping() # create object
        hopp.m = superhopping(dr=dr) # get hopping of the supercell
        hopp.dir = dr
        if not np.sum(np.abs(hopp.m))==0: # skip this matrix
          hoppings.append(hopp)
        else: pass
      hr.hopping = hoppings # store the list
  return hr 



def derivative(h,k,order=[1,0]):
  """Calculate the derivative of the Hamiltonian"""
  if derivative < 1: raise
  if h.is_multicell==False: raise
  if h.dimensionality == 0: return None
  if h.dimensionality == 1: # one dimensional
      mout = h.intra*0.0 # initialize
      for t in h.hopping: # loop over matrices
        phi = t.dir[0]*k # phase
        pref = (dir[0]*1j)**order[0] # prefactor
        tk = t*pref*t.m * np.exp(1j*np.pi*2.*phi) # k hopping
        mout = mout + tk # add contribution
      return mout
  if h.dimensionality == 2: # two dimensional
      k = np.array([k[0],k[1]]) # convert to array
      mout = h.intra*0.0 # initialize
      for t in h.hopping: # loop over matrices
        d = t.dir
        d = np.array([d[0],d[1]]) # vector director of hopping
        phi = d.dot(k) # phase
        pref1 = (d[0]*1j)**order[0] # prefactor
        pref2 = (d[1]*1j)**order[1] # prefactor
        pref = pref1*pref2 # total prefactor
        tk = pref*t.m * np.exp(1j*np.pi*2.*phi) # derivative of the first
        mout = mout + tk # add to the hamiltonian
      return mout









def first_neighbors(h):
  """ Gets a first neighbor hamiltonian"""
  from hamiltonians import create_fn_hopping
  r = h.geometry.r    # x coordinate 
  g = h.geometry
  h.is_multicell = True 
# first neighbors hopping, all the matrices
  a1, a2, a3 = g.a1, g.a2, g.a3
  h.intra = create_fn_hopping(r,r) # intra matrix
  h.hopping = [] # empty list
  for i1 in [-1,0,1]:
    for i2 in [-1,0,1]:
      for i3 in [-1,0,1]:
        if i1==0 and i2==0 and i3==0: continue
        t = Hopping() # hopping class
        da = a1*i1+a2*i2+a3*i3 # direction
        t.m = create_fn_hopping(r,r+a1)
        t.dir = [i1,i2,i3] # store direction
        h.hopping.append(t) # append 
  return h
