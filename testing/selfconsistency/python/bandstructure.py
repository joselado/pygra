
# special band structures

import topology
import operators
import scipy.linalg as lg
import numpy as np


def berry_bands(h,klist=None,mode=None,operator=None):
  """Calculate band structure resolved with Berry curvature"""
  ks = [] # list of kpoints
  if mode is not None: # get the mode
    if mode=="sz": operator = operators.get_sz(h)
    else: raise

  fo = open("BANDS.OUT","w")
  for ik in range(len(klist)): # loop over kpoints
    (es,bs) = topology.operator_berry_bands(h,k=klist[ik],operator=operator)
    for (e,b) in zip(es,bs):
      fo.write(str(ik)+"    "+str(e)+"    "+str(b)+"\n")
  fo.close()



def current_bands(h,klist=None):
  """Calcualte the band structure, with the bands"""
  if h.dimensionality != 1: raise # only 1 dimensional
  hkgen = h.get_hk_gen() # get generator of the hamiltonian
  if klist is None:  klist = np.linspace(0,1.,100) # generate k points
  fo = open("BANDS.OUT","w") # output file
  for k in klist: # loop over kpoints
    hk = hkgen(k) # get k-hamiltonian
    phik = np.exp(1j*2.*np.pi*k) # complex phase
    jk = 1j*(h.inter*phik - h.inter.H*np.conjugate(phik)) # current 
    evals,evecs = lg.eigh(hk) # eigenvectors and eigenvalues
    evecs = np.transpose(evecs) # transpose eigenvectors
    for (e,w) in zip(evals,evecs): # do the loop
        w = np.matrix(w) # convert to matrix
        waw = (w.T).H*jk*w.T # expectation value
        waw = waw[0,0].real # real part
        fo.write(str(k)+"    "+str(e)+"   "+str(waw)+"\n")
  fo.close()












def get_bands_0d(h,operator=None):
  """ Returns a figure with the bandstructure of the system"""
  if h.is_sparse:
    energies = lg.eigvalsh(h.intra.todense()) # eigenvalues
  else:
    if operator is None: energies = lg.eigvalsh(h.intra) # eigenvalues
    else: # matrix
      energies,ws = lg.eigh(h.intra)
      vals = []
      ws = np.transpose(ws) # transpose
      for w in ws: # loop over waves
        w = np.matrix(w) # convert to matrix
        waw = (w.T).H*operator*w.T # expectation value
        waw = waw[0,0].real # real part
        vals.append(waw) # store
  klist = np.linspace(0,1,len(energies))
  if operator is None: msave = np.matrix([klist,energies]).T
  else: msave = np.matrix([klist,energies,vals]).T
  np.savetxt("BANDS.OUT",msave) # save all
  return np.genfromtxt("BANDS.OUT").transpose() # return data







def get_bands_1d(h,nkpoints=100,operator=None,num_bands=None):
  if num_bands is None: # all the bands
    if operator is not None: diagf = lg.eigh # all eigenvals and eigenfuncs
    else: diagf = lg.eigvalsh # all eigenvals and eigenfuncs
  else: # using arpack
    h.turn_sparse() # sparse Hamiltonian
    def diagf(m):
      eig,eigvec = slg.eigsh(m,k=num_bands,which="LM",sigma=0.0)
      if operator is None: return eig
      else: return (eig,eigvec)
  hkgen = h.get_hk_gen() # generator hamiltonian
  ks = np.linspace(0.,1.,nkpoints)
  f = open("BANDS.OUT","w") # open bands file
  f.write("# system_dimension = 1\n")
  if operator!=None: operator=np.matrix(operator) # convert to matrix
  for k in ks: # loop over kpoints
    print("Doing ",k)
    hk = hkgen(k) # get hamiltonian
#    if h.is_sparse: hk = hk.todense() # turn the matrix dense
    if operator is None:
      es = diagf(hk)
      for e in es:  # loop over energies
        f.write(str(k)+"   "+str(e)+"\n") # write in file
    else:
      es,ws = diagf(hk)
      ws = ws.transpose() # transpose eigenvectors
      for (e,w) in zip(es,ws):  # loop over waves
        w = np.matrix(w) # convert to matrix
        waw = (w.T).H*operator*w.T # expectation value
        waw = waw[0,0].real # real part
        f.write(str(k)+"   "+str(e)+"  "+str(waw)+"\n") # write in file
  f.close()
  return np.genfromtxt("BANDS.OUT").transpose() # return data



def get_bands_2d(h,kpath=None,operator=None,num_bands=None):
  """Get a 2d bandstructure"""
  if num_bands is None: # all the bands
    if operator is not None: diagf = lg.eigh # all eigenvals and eigenfuncs
    else: diagf = lg.eigvalsh # all eigenvals and eigenfuncs
  else: # using arpack
    h.turn_sparse() # sparse Hamiltonian
    def diagf(m):
      eig,eigvec = slg.eigsh(m,k=num_bands,which="LM",sigma=0.0)
      if operator is None: return eig
      else: return (eig,eigvec)
  # open file and get generator
  f = open("BANDS.OUT","w") # open bands file
  hkgen = h.get_hk_gen() # generator hamiltonian
  if operator is not None: operator=np.matrix(operator) # convert to matrix
  if kpath is None:
    import klist
    kpath = klist.default(h.geometry) # generate default klist
  for k in range(len(kpath)): # loop over kpoints
    print("Doing kpoint",k)
    hk = hkgen(kpath[k]) # get hamiltonian
    if operator is None:
      es = diagf(hk)
      for e in es:  # loop over energies
        f.write(str(k)+"   "+str(e)+"\n") # write in file
    else:
      es,ws = diagf(hk)
      ws = ws.transpose() # transpose eigenvectors
      for (e,w) in zip(es,ws):  # loop over waves
        w = np.matrix(w) # convert to matrix
        waw = (w.T).H*operator*w.T # expectation value
        waw = waw[0,0].real # real part
        f.write(str(k)+"   "+str(e)+"  "+str(waw)+"\n") # write in file
  f.close()
  return np.genfromtxt("BANDS.OUT").transpose() # return data

