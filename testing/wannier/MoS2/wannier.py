# routines to work with wannier hamiltonians

import numpy as np
import hamiltonians
import geometry


def read_geometry(input_file="wannier.win"):
  """Reads the geometry of the wannier calculation"""
  ll = read_between("begin unit_cell_cart","end unit_cell_cart",input_file)
  a1 = ll[1].split()
  a2 = ll[2].split()
  a3 = ll[3].split()
  # read the unit vectors
  a1 = np.array([float(a1[0]),float(a1[1]),float(a1[2])]) # first vector
  a2 = np.array([float(a2[0]),float(a2[1]),float(a2[2])]) # second vector
  a3 = np.array([float(a3[0]),float(a3[1]),float(a3[2])]) # second vector
  g = geometry.geometry()
  g.dimensionality = 2
  g.has_spin = False
  g.has_sublattice = False
  g.a1 = a1  # store vector
  g.a2 = a2  # store vector
  # read the coordinates 
  ll = read_between("begin projections","end projections",input_file)
  rs = [] # empty list for positions
  for l in ll:
    name = l.split(":")[0] # get name of hte atom
    r = get_positions(name,input_file) # get positins of the atoms
    for i in range(len(r)): # to real coordinates
      r[i] = r[i][0]*a1 + r[i][1]*a2 + r[i][2]*a3
    rs += r # store positions
  g.r = np.array(rs) # store in the class
  g.r2xyz() # store also in xyz atributes
  return g


def get_positions(atom,input_file):
  """Get positions of certain orbitals"""
  ll = read_between("begin atoms_frac","end atoms_frac",input_file)
  rs = [] # empty list
  for l in ll: # loop over lines
    l = l.split()
    name = l[0]
    if atom==name: # found atom
      r = np.array([float(l[1]),float(l[2]),float(l[3])]) # position
      rs.append(r) # add to the list
  return rs # return positions





def read_between(a,b,input_file):
  ll = open(input_file).readlines()
  start = False # found the klist
  out = []
  for (i,l) in zip(range(len(ll)),ll):
    if b in l: break # end of klist
    if start: # sotre line
      out.append(l)
    if a in l: start = True # found beginning 
  return out # return output lines





def read_hamiltonian(input_file="hr_truncated.dat"):
  """Reads an output hamiltonian from wannier"""
  mt = np.genfromtxt(input_file) # get file
  m = mt.transpose() # transpose matrix
  # read the hamiltonian matrices
  class Hopping: pass # create empty class
  tlist = []
  def get_t(i,j,k):
    norb = np.max([np.max(np.abs(m[3])),np.max(np.abs(m[4]))])
    mo = np.matrix(np.zeros((norb,norb),dtype=np.complex))  
    for l in mt: # look into the file
      if i==int(l[0]) and j==int(l[1]) and k==int(l[2]):
        mo[int(l[3])-1,int(l[4])-1] = l[5] + 1j*l[6] # store element
    return mo # return the matrix
#  for i in range(-nmax,nmax):
#    for j in range(-nmax,nmax):
#      for k in range(-nmax,nmax):
#        t = Hopping() # create hopping
#        t.dir = [i,j,k] # direction
#        t.m = get_t(i,j,k) # read the matrix
#        tlist.append(t) # store hopping
  # the previous is not used yet...
  g = geometry.kagome_lattice() # create geometry
  h = g.get_hamiltonian() # build hamiltonian
  h.intra = get_t(0,0,0)
  h.tx = get_t(1,0,0)
  h.ty = get_t(0,1,0)
  h.txy = get_t(1,1,0)
  h.txmy = get_t(1,-1,0)
  h.has_spin = False  # if not spin polarized
  h.geometry = read_geometry() # read the geometry of the system
  if len(h.geometry.r)!=len(h.intra): 
    print "Dimensions do not match",len(g.r),len(h.intra)
    print h.geometry.r
    raise # error if dimensions dont match
  return h





def get_klist(input_file="wannier.win"):
  """ Get the klist for bands calculation"""
  ll = read_between("begin kpoint_path","end kpoint_path",input_file)
  kp = [] # empty vertex
  for l in ll: 
    l2 = l.split() # split the numbers
    kp.append([[float(l2[1]),float(l2[2]),float(l2[3])],[float(l2[5]),float(l2[6]),float(l2[7])]])
  klist = [] # empty klist
  nk = 500/len(kp) # number of kpoints
  for (k1,k2) in kp: # loop over pairs
    k1 = np.array(k1)
    k2 = np.array(k2)
    dk = (k2-k1)/nk # create dk
    for i in range(nk): # loop over ks
      klist.append(k1+i*dk)
  return klist



