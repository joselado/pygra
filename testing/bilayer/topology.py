# library to calculate topological properties

import numpy as np
from scipy.sparse import bmat, csc_matrix
import scipy.linalg 

def majorana_invariant(intra,inter,kp=1000):
  """ Calculates the topological invariant for a 1d topological
  superconductor, returns a list of determinants of the upper diagonal"""
  ks = np.arange(0.5,1.5,1.0/kp) # create kpoints
  dets = [0. for k in ks]  # create list with determinants
  # rotate the matrices into a non diagonal block for
  # assume that h = sz*h_0 + i sy * h_delta
  # and perfor a rotation e^-i*pi/4 sy
  rot = intra * 0.0
  n = len(intra)/2 # number of orbitals including spin
  # create rotation matrix
  intra_a = np.matrix([[0.0j for i in range(n)] for j in range(n)])
  inter_a = np.matrix([[0.0j for i in range(n)] for j in range(n)])
  print csc_matrix(intra-intra.H)
  for i in range(n):
    for j in range(n):
      # couples electron in i with hole in j
      s = 1.0
      if i<j:
        s = -1.0
      intra_a[i,j] = 1j*s*intra[2*i,2*j+1] + intra[2*i,2*j]
#      intra_a[i,j] = intra[2*i,2*j+1]
      inter_a[i,j] = 1j*s*inter[2*i,2*j+1] + inter[2*i,2*j]
#  print csc_matrix(intra_a)
  fm = open("WINDING_MAJORANA.OUT","w")
  fm.write("# kpoint,     phase")
  for k in ks:
    tk = inter_a * np.exp(1j*2.*np.pi*k)
    hk = intra_a + tk + tk.H # kdependent k
    det = scipy.linalg.det(hk)
    phi = np.arctan2(det.imag,det.real)
    fm.write(str(k)+"    "+str(phi)+"\n")
  fm.close()  # close the file

