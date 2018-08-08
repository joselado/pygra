import scipy.linalg as lg
import scipy.sparse.linalg as slg
from scipy.sparse import csc_matrix,eye
import numpy as np

def correlator0d(m,energies=np.linspace(-10.,10.,400),i=0,j=0,delta=0.07):
  """Calculate a certain correlator"""
  iden = np.identity(m.shape[0],dtype=np.complex)
  zs = np.zeros(energies.shape[0],dtype=np.complex)
  for (ie,e) in zip(range(len(energies)),energies):
    m0 = ((e+1j*delta)*iden - m).I # inverse 
    zs[ie] = m0[i,j]
  np.savetxt("CORRELATOR.OUT",np.matrix([energies,-zs.imag,zs.real]).T)



def gij(m,i=0,delta=0.01,e=0.0):
  """Calculate a single row of the Green function"""
  v0 = np.zeros(m.shape[0])
  v0[i] = 1.
  iden = eye(v0.shape[0]) # identity matrix
  g = iden*(e+1j*delta) - csc_matrix(m) # matrix to invert
#  print(type(g)) ; exit()
  (b,info) = slg.lgmres(g,v0) # solve the equation  
  go = (b*np.conjugate(b)).real
  return go



