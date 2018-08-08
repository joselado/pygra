import numpy as np


def add_peierls(h,mag_field=0.0):
  """ Adds Peierls phase to the Hamiltonian"""
  x = h.geometry.x    # x coordinate 
  y = h.geometry.y    # x coordinate 
  a1 = h.geometry.a1    # distance to neighboring cell
  celldis = np.sqrt(a1.dot(a1))
  from numpy import array
  norb = h.intra.shape[0]  # number of orbitals
  if h.is_sparse: # sparse hamiltonian
    from scipy.sparse import coo_matrix,csc_matrix
    if True: # zero dimensional
      m = coo_matrix(h.intra) # convert to sparse matrix
      row,col = m.row,m.col
      data = m.data +0j
      for k in range(len(m.data)): # loop over non vanishing elements
        i = m.row[k]
        j = m.col[k]
        if h.has_spin: i,j = i/2,j/2 # raise if spinful
        p = peierls(x[i],y[i],x[j],y[j],mag_field) # peierls phase
        data[k] *= p # add phase
      h.intra = csc_matrix((data,(row,col)),shape=(norb,norb)) # convert to csc
    if h.dimensionality==1: # one dimensional
      # check that celldis is right
      if np.abs(celldis - h.geometry.a1[0])>0.001: raise
      def phaseize(inter,numn=1):
        m = coo_matrix(inter) # convert to sparse matrix
        row,col = m.row,m.col
        data = m.data +0j
        for k in range(len(m.data)): # loop over non vanishing elements
          i = m.row[k]
          j = m.col[k]
          if h.has_spin: i,j = i/2,j/2 # raise if spinful
          # peierls phase
          p = peierls(x[i],y[i],x[j]+numn*celldis,y[j],mag_field) 
          data[k] *= p # add phase
        return csc_matrix((data,(row,col)),shape=(norb,norb)) # convert to csc
      # for normal hamiltonians
      if not h.is_multicell: h.inter = phaseize(h.inter,numn=1) 
      # for multicell hamiltonians
      if h.is_multicell: 
        hopping = [] # empty list
        for i in range(len(h.hopping)):
          h.hopping[i].m = phaseize(h.hopping[i].m,numn=h.hopping[i].dir[0]) 
    if h.dimensionality>1: raise # error if greater than 1
  else: # not sparse
    def gaugeize(m,d=0.0):
      """Add gauge phase to a matrix"""
      for i in range(len(x)):
        for j in range(len(x)):
          p = peierls(x[i],y[i],x[j]+d,y[j],mag_field) # peierls phase
          if h.has_spin:
            m[2*i,2*j] *= p
            m[2*i,2*j+1] *= p
            m[2*i+1,2*j] *= p
            m[2*i+1,2*j+1] *= p
          else:
            m[i,j] *= p
    gaugeize(h.intra,d=0.0)  # gaugeize intraterm
    if h.dimensionality==0: pass # if zero dimensional
    elif h.dimensionality==1: # if one dimensional
      if h.is_multicell: raise
      gaugeize(h.inter,d=celldis) # gaugeize interterm
    elif h.dimensionality==2: # if bigger dimensional
      print("WARNING, is your gauge periodic?")
      gaugeize(h.tx,d=h.geometry.a1[0]) # gaugeize interterm
    else:
      raise




def peierls(x1,y1,x2,y2,mag_field):
  """ Returns the complex phase with magnetic field """
  if is_number(mag_field): # if it is a number assumen Landau gauge
    phase = mag_field*(x1-x2)*(y1+y2)/2.0
  elif callable(mag_field): # if it is callable 
    phase = mag_field(x1,y1,x2,y2)  # specific call to the value
  else:  # if anything else error
    raise
  return np.exp(1j*phase)



def is_number(s):
    try:
        float(s)
        return True
    except:
        return False

