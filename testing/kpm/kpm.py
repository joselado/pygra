# kernel polynomial method libraries
from __future__ import print_function,division
import scipy.sparse.linalg as lg
from scipy.sparse import csc_matrix as csc
import numpy.random as rand
from scipy.sparse import coo_matrix,csc_matrix,bmat
import numpy as np
from scipy.signal import hilbert

# check that the fortran library exists
try: 
  import kpmf90 
  use_fortran = True
except:
  use_fortran = False # use python routines
  print("FORTRAN library not present, using default python one")




def get_moments(v,m,n=100,use_fortran=use_fortran):
  """ Get the first n moments of a certain vector
  using the Chebychev recursion relations"""
  if use_fortran:
    from kpmf90 import get_momentsf90 # fortran routine
    mo = coo_matrix(m) # convert to coo matrix
    vo = v.todense() # convert to conventional vector
    vo = np.array([vo[i,0] for i in range(len(vo))])
# call the fortran routine
    mus = get_momentsf90(mo.row+1,mo.col+1,mo.data,vo,n) 
    return mus # return fortran result
  else:
   return python_kpm_moments_clear(v,m,n=n)
   return python_kpm_moments(v,m,n=n)


def python_kpm_moments(v,m,n=100):
  """Python routine to calculate moments"""
  mus = np.array([0.0j for i in range(2*n)]) # empty arrray for the moments
  a = v.copy() # first vector
  am = v.copy() # zero vector
  a = m*v  # vector number 1
  bk = (np.transpose(np.conjugate(v))*v)[0,0] # scalar product
  bk1 = (np.transpose(np.conjugate(v))*a)[0,0] # scalar product
  mus[0] = bk  # mu0
  mus[1] = bk1 # mu1
  for i in range(1,n): 
    ap = 2*m*a - am # recursion relation
    bk = (np.transpose(np.conjugate(a))*a)[0,0] # scalar product
    bk1 = (np.transpose(np.conjugate(ap))*a)[0,0] # scalar product
    mus[2*i] = 2.*bk
    mus[2*i+1] = 2.*bk1
    am = a +0. # new variables
    a = ap+0. # new variables
  mu0 = mus[0] # first
  mu1 = mus[1] # second
  for i in range(1,n): 
    mus[2*i] +=  - mu0
    mus[2*i+1] += -mu1 
  return mus


def python_kpm_moments_clear(v,m,n=100):
  """Python routine to calculate moments"""
  mus = np.array([0.0j for i in range(2*n)]) # empty arrray for the moments
  a0 = v.copy() # first vector
  am = v.copy() # first vector
  a = m*v  # vector number 1
  mus[0] = 1.  # mu0
  mu = (np.transpose(np.conjugate(a0))*a)[0,0] # scalar product
  mus[1] = mu # mu1
  for i in range(1,2*n): 
    ap = 2*m*a - am # recursion relation
    mu = (np.transpose(np.conjugate(a0))*a)[0,0] # scalar product
    mus[i] = mu # store
    am = a.copy() # new variables
    a = ap.copy() # new variables
  mu0 = mus[0] # first
  mu1 = mus[1] # second
  return mus






def get_momentsA(v,m,n=100,A=None):
  """ Get the first n moments of a certain vector
  using the Chebychev recursion relations"""
  mus = np.array([0.0j for i in range(n)]) # empty arrray for the moments
  am = v.copy() # zero vector
  a = m*v  # vector number 1
  bk = (np.transpose(np.conjugate(v))*A*v)[0,0] # scalar product
  bk1 = (np.transpose(np.conjugate(a))*A*v)[0,0] # scalar product
  mus[0] = bk  # mu0
  mus[1] = bk1 # mu1
  for i in range(2,n): 
    ap = 2.*m*a - am # recursion relation
    bk = (np.transpose(np.conjugate(ap))*A*v)[0,0] # scalar product
    mus[i] = bk
    am = a.copy() # new variables
    a = ap.copy() # new variables
  mu0 = mus[0] # first
  mu1 = mus[1] # second
  return mus




def get_moments_ij(m0,n=100,i=0,j=0,use_fortran=use_fortran):
  """ Get the first n moments of a the |i><j| operator
  using the Chebychev recursion relations"""
  m = coo_matrix(m0,dtype=np.complex)
  if use_fortran:
    mus = kpmf90.get_moments_ij(m.row+1,m.col+1,m.data,n,m.shape[0],i+1,j+1)
    return mus
  else:
    mus = np.zeros(n) # empty arrray for the moments
    v = np.zeros(m.shape[0]) ; v[i] = 1.0 # initial vector
    v = np.matrix([v]).T # zero vector
    am = v.copy()
    a = m*v  # vector number 1
    bk = v[j] # scalar product
    bk1 = a[j,0] # scalar product
    mus[0] = bk  # mu0
    mus[1] = bk1 # mu1
    for ii in range(2,n): 
      ap = 2.*m*a - am # recursion relation
      bk = ap[j,0] # scalar product
      mus[ii] = bk
      am = a.copy() # new variables
      a = ap.copy() # new variables
    return mus








def full_trace(m_in,n=200,use_fortran=True):
  """ Get full trace of the matrix"""
  m = csc(m_in) # saprse matrix
  nd = m.shape[0] # length of the matrix
  mus = np.array([0.0j for i in range(2*n)])
#  for i in range(ntries):
  for i in range(nd):
    mus += local_dos(m_in,i=i,n=n,use_fortran=use_fortran)
  return mus/nd









def local_dos(m_in,i=0,n=200,use_fortran=True):
  """ Calculates local DOS using the KPM"""
  m = csc(m_in) # saprse matrix
  nd = m.shape[0] # length of the matrix
  mus = np.array([0.0j for j in range(2*n)])
  v = rand.random(nd)*0.
  v[i] = 1.0 # vector only in site i 
  v = csc(v).transpose()
# get the chebychev moments
  mus += get_moments(v,m,n=n,use_fortran=use_fortran) 
  return mus



def ldos0d(m_in,i=0,scale=10.,npol=None,ne=500,kernel="jackson"):
  """Return two arrays with energies and local DOS"""
  if npol is None: npol = ne
  mus = local_dos(m_in/scale,i=i,n=npol) # get coefficients
  xs = np.linspace(-1.0,1.0,ne,endpoint=True)*0.99 # energies
  ys = generate_profile(mus,xs,kernel=kernel)
  return (scale*xs,ys/scale)



def tdos0d(m_in,scale=10.,npol=None,ne=500,kernel="jackson",ntries=20):
  """Return two arrays with energies and local DOS"""
  if npol is None: npol = ne
  mus = random_trace(m_in/scale,ntries=ntries,n=npol) # get coefficients
  xs = np.linspace(-1.0,1.0,ne,endpoint=True)*0.99 # energies
  ys = generate_profile(mus,xs,kernel=kernel)
  return (scale*xs,ys/scale)


def random_trace(m_in,ntries=20,n=200,fun=None):
  """ Calculates local DOS using the KPM"""
  if fun is not None: # check that dimensions are fine
    v0 = fun()
    if len(v0) != m_in.shape[0]: raise
  if fun is None:
    def fun(): return rand.random(nd) -.5 + 1j*rand.random(nd) -.5j
  m = csc(m_in) # saprse matrix
  nd = m.shape[0] # length of the matrix
  mus = np.array([0.0j for j in range(2*n)])
  for i in range(ntries): # loop over tries
    v = fun()
    v = v/np.sqrt(v.dot(np.conjugate(v))) # normalize the vector
    v = csc(v).transpose()
    mus += get_moments(v,m,n=n) # get the chebychev moments
  return mus/ntries



def random_trace_A(m_in,ntries=20,n=200,A=None):
  """ Calculates local DOS using the KPM"""
  m = csc(m_in) # saprse matrix
  nd = m.shape[0] # length of the matrix
  mus = np.array([0.0j for j in range(n)])
  for i in range(ntries): # loop over tries
    #v = rand.random(nd) - .5
    v = rand.random(nd) -.5 + 1j*rand.random(nd) -.5j
    v = v/np.sqrt(v.dot(v)) # normalize the vector
    v = csc(v).transpose()
    mus += get_momentsA(v,m,n=n,A=A) # get the chebychev moments
  return mus/ntries



def full_trace_A(m_in,ntries=20,n=200,A=None):
  """ Calculates local DOS using the KPM"""
  m = csc(m_in) # saprse matrix
  nd = m.shape[0] # length of the matrix
  mus = np.array([0.0j for j in range(2*n)])
  for i in range(nd): # loop over tries
    #v = rand.random(nd) - .5
    v = rand.random(nd)*0.
    v[i] = 1.0 # vector only in site i 
    v = csc(v).transpose()
    mus += get_momentsA(v,m,n=n,A=A) # get the chebychev moments
  return mus/nd



def correlator0d(m_in,i=0,j=0,scale=10.,npol=None,ne=500):
  """Return two arrays with energies and local DOS"""
  if npol is None: npol = ne
  mus = get_moments_ij(m_in/scale,n=npol,i=i,j=j)
  xs = np.linspace(-1.0,1.0,ne,endpoint=True)*0.99 # energies
  ys = generate_profile(mus,xs,kernel="jackson")/scale*np.pi # so it is the Green function
  imys = hilbert(ys).imag
#  np.savetxt("CORRELATOR.OUT",np.matrix([scale*xs,ys,imys]).T)
  return (scale*xs,-imys,ys)





def generate_profile(mus,xs,kernel="jackson",use_fortran=use_fortran):
  """ Uses the Chebychev expansion to create a certain profile"""
  # initialize polynomials
#  xs = np.array([0.])
  tm = xs.copy()*0. +1.
  t = xs.copy()
  ys = mus[0] # first term
  if kernel=="jackson": mus = jackson_kernel(mus)
  elif kernel=="lorentz": mus = lorentz_kernel(mus)
  else: raise
  if use_fortran: # call the fortran routine
    ys = kpmf90.generate_profile(mus,xs) 
  else: # do a python loop
    # loop over all contributions
    for i in range(1,len(mus)):
      mu = mus[i]
      ys += 2.*mu*t # add contribution
      tp = 2.*xs*t - tm # chebychev recursion relation
      tm = t + 0.
      t = 0. + tp # next iteration
    ys = ys/np.sqrt(1.-xs*xs) # prefactor
  ys = ys.real/np.pi
  return ys


def dos(m_in,xs,ntries=20,n=200,scale=10.):
  """Return the density of states"""
  if scale is None: scale = 10.*np.max(np.abs(m_in.data)) # estimate of the value
  mus = random_trace(m_in/scale,ntries=ntries,n=n)
  ys = generate_profile(mus,xs/scale) # generate the DOS
  return ys # return the DOS 



def jackson_kernel(mus):
  """ Modify coeficient using the Jackson Kernel"""
  mo = mus.copy() # copy array
  n = len(mo)
  pn = np.pi/(n+1.) # factor
  for i in range(n):
    fac = ((n-i+1)*np.cos(pn*i)+np.sin(pn*i)/np.tan(pn))/(n+1)
    mo[i] *= fac
  return mo



def lorentz_kernel(mus):
  """ Modify coeficient using the Jackson Kernel"""
  mo = mus.copy() # copy array
  n = len(mo)
  pn = np.pi/(n+1.) # factor
  lamb = 3.
  for i in range(n):
    fac = np.sinh(lamb*(1.-i/n))/np.sinh(lamb)
    mo[i] *= fac
  return mo





def fejer_kernel(mus):
  """Default kernel"""
  n = len(mus)
  mo = mus.copy()
  for i in range(len(mus)):
    mo[i] *= (1.-float(i)/n) 
  return mo



def edge_dos(intra0,inter0,scale=4.,w=20,npol=300,ne=500,bulk=False,
                use_random=True,nrand=20):
  """Calculated the edge DOS using the KPM"""
  h = [[None for j in range(w)] for i in range(w)]
  intra = csc_matrix(intra0)
  inter = csc_matrix(inter0)
  for i in range(w): h[i][i] = intra
  for i in range(w-1): 
    h[i+1][i] = inter.H
    h[i][i+1] = inter
  h = bmat(h) # sparse hamiltonian
  ds = np.zeros(ne)
  dsb = np.zeros(ne)
  norb = intra0.shape[0] # orbitals ina cell
  for i in range(norb):
    (xs,ys) = ldos0d(h,i=i,scale=scale,npol=npol,ne=ne) 
    ds += ys # store
    if bulk:
      (xs,zs) = ldos0d(h,i=w*norb//2 + i,scale=scale,npol=npol,ne=ne) 
      dsb += zs # store
  if not bulk: return (xs,ds/w)
  else: return (xs,ds/w,dsb/w)








