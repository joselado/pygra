from __future__ import print_function
import scipy.sparse.linalg as lg
from scipy.sparse import csc_matrix
from scipy.sparse import coo_matrix,bmat
import time
import numpy as np


def directional_mean_field(vecs):
  """ Creates an initial mean field accoring to certain vectors"""
  from hamiltonians import sx,sy,sz
  mf = [[None for i in vecs] for j in vecs] # create
  for i in range(len(vecs)):
    v = vecs[i]
    mf[i][i] = v[0]*sx + v[1]*sy + v[2]*sz # add contribution
  return bmat(mf).todense()




def hubbardscf(h,U=1.0,nkp = 100,filling=0.5,mag=None,mix=0.5,
                  maxerror=1e-06,silent=False,mf=None,
                  smearing=None,collinear=False):
  """ Solve a selfocnsistent Hubbard mean field"""
  from scipy.linalg import eigh
  import correlatorsf90
  nat = h.intra.shape[0]//2 # number of atoms
  htmp = h.copy()  # copy hamiltonian
  # generalate the necessary list of correlators
  if mf is None: # generate initial mean field
    if mag is None: mag = np.random.random((nat,3)) 
    old_mf = U*directional_mean_field(mag) # get mean field matrix
  else: old_mf = mf # use guess
  # get the pairs for the correlators
  ndim = h.intra.shape[0] # dimension
  totkp = nkp**(h.dimensionality) # total number of kpoints
  while True: # infinite loop
    htmp.intra = h.intra + old_mf # add mean field 
    t1 = time.perf_counter()
    eigvals,eigvecs = htmp.eigenvectors(nkp) # get eigenvectors
    # get the fermi energy
    ne = len(eigvals) ; ifermi = int(round(ne*filling)) # index for fermi
    sorte = np.sort(eigvals) # sorted eigenvalues
    fermi = (sorte[ifermi-1] + sorte[ifermi])/2. # fermi energy
    if smearing is None: # no smearing
      voccs = [] # accupied vectors
      eoccs = [] # accupied eigenvalues
      for (e,v) in zip(eigvals,eigvecs): # loop over eigenvals,eigenvecs
        if e<fermi:  # if level is filled, add contribution
          voccs.append(v) # store
          eoccs.append(e) # store
      voccs = np.matrix(np.array(voccs))  # as array
      eoccs = np.array(eoccs)  # as array
    t2 = time.perf_counter()
    # get the necessary expectation values and matrices
    (vdup,vddn,vxc,ndn,nup,xc) = get_udxc(voccs,totkp=totkp) # density and XC
    # full mean field matrix
    if collinear: mf = ndn + nup 
    else: mf = ndn + nup - xc - xc.H
    t3 = time.perf_counter()
#    print("Times",t2-t1,t3-t2)
    mf = U*mf.todense() # new intramatrix
    error = np.max(np.abs(old_mf-mf)) # absolute difference
    # total energy
    etot = np.sum(eoccs)/totkp  # eigenvalues
    etot -= U*np.sum(vdup*vddn).real # density DC
    etot += U*np.sum(vxc*np.conjugate(vxc)).real # exchange DC
    totcharge = np.sum(vdup+vddn).real # total charge
    avcharge = totcharge/nat # average charge
    ######
    if not silent:
      print("Error in SCF =",error)
      print("Fermi energy =",fermi)
      print("Total energy =",etot)
      print("Total charge =",totcharge)
      print("Average charge =",avcharge)
    old_mf = old_mf*mix + mf*(1.-mix) # mixing
    if error<maxerror: # if converged break
      break
  # output result
  class scfclass(): pass
  scf = scfclass() # empty class
  scf.hamiltonian = htmp.copy() # copy Hamiltonian
  scf.hamiltonian.intra -= fermi*np.identity(ndim) # shift Fermi energy
  scf.energy = etot # store total energy
  scf.mean_field = mf # store mean field matrix
  scf.magnetization = np.array([vxc.real,vxc.imag,vdup-vddn]).transpose().real
  write_magnetization(scf.magnetization) # write in file
  return scf # return mean field






def get_udxc(voccs,weight=None,totkp=1):
  """Get up/down densities and corresponding mean field matrices"""
  import correlatorsf90
  ndim = voccs.shape[1] # dimension of the matrix
  if weight is not None:
    if len(weight)!=voccs.shape[0]: raise # inconsistent dimensions
  nat = ndim//2 # one half
  pdup = np.array([[2*i,2*i] for i in range(nat)]) # up density
  pddn = pdup + 1 # down density
  pxc = np.array([[2*i,2*i+1] for i in range(nat)]) # exchange
  if weight is None: # no weight
    vdup = correlatorsf90.correlators(voccs,pdup)/totkp
    vddn = correlatorsf90.correlators(voccs,pddn)/totkp
    vxc = correlatorsf90.correlators(voccs,pxc)/totkp
  else: # with weight
    vdup = correlatorsf90.correlators_weighted(voccs,weight,pdup)/totkp
    vddn = correlatorsf90.correlators_weighted(voccs,weight,pddn)/totkp
    vxc = correlatorsf90.correlators_weighted(voccs,pxc)/totkp
  ndn = csc_matrix((vdup,pddn.transpose()),dtype=np.complex,shape=(ndim,ndim))
  nup = csc_matrix((vddn,pdup.transpose()),dtype=np.complex,shape=(ndim,ndim))
  xc = csc_matrix((np.conjugate(vxc),pxc.transpose()),
                           dtype=np.complex,shape=(ndim,ndim))
  return (vdup,vddn,vxc,ndn,nup,xc) # return everything








def write_magnetization(mag):
  """Write magnetization in a file"""
  fo = open("MAGNETIZATION.OUT","w")
  ix = 1
  for m in mag:
    fo.write(str(ix)+"  ")
    fo.write(str(m[0])+"  ")
    fo.write(str(m[1])+"  ")
    fo.write(str(m[2])+"\n")
    ix += 1
  fo.close()

