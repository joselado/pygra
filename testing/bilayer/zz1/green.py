# functions to wrap around fortran code


import pylab as py
import numpy as np
import numpy as np


class gf_convergence():
   """ Class to manage the convergence  options
   of the green functions """
   optimal = True
   refinement = False
   guess = True # use old green function
   def __init__(self,mode):
     if mode=="fast":   # fast mode,used for coule to finite systems 
       self.eps = 0.001
       self.max_error = 1.0
       self.num_rep = 10
       self.mixing = 1.0
     if mode=="lead":
       self.eps = 0.00001
       self.max_error = 0.00001
       self.num_rep = 3
       self.mixing = 0.7
     if mode=="hundred":  
       self.eps = 0.001
       self.max_error = 1.0
       self.num_rep = 100
       self.mixing = 1.0



def dyson(intra,inter,energy=0.0,gf=None,is_sparse=False,initial = None):
  """ Solves the dyson equation for a one dimensional
  system with intra matrix 'intra' and inter to the nerest cell
  'inter'"""
  # get parameters
  if gf == None: gf = gf_convergence("fast")
  mixing = gf.mixing
  eps = gf.eps
  max_error = gf.max_error
  num_rep = gf.num_rep
  optimal = gf.optimal
  try:
    intra = intra.todense()
    inter = inter.todense()
  except:
    a = 1
  if initial==None:  # if green not provided. initialize at zero
    from numpy import zeros
   
    g_guess = intra*0.0j
  else:
    g_guess = initial
  # calculate using fortran
  if optimal:
    print "Fortran dyson calculation"
    from green_fortran import dyson  # import fortran subroutine
    (g,num_redo) = dyson(intra,inter,energy,num_rep,mixing=mixing,
               eps=eps,green_guess=g_guess,max_error=max_error)
    print "      Converged in ",num_redo,"iterations\n"
    from numpy import matrix
    g = matrix(g)
  # calculate using python
  if not optimal:
    g_old = g_guess # first iteration
    ec = energy+1j*eps # complex energy
    iden = np.matrix(np.identity(len(intra),dtype=complex)) # create identity
    for i in range(num_rep): # loop over iterations
      self = inter*g_old*inter.H # selfenergy
      g = (iden*ec - intra - self).I # dyson equation
      g_old = mixing*g + (1-mixing)*g_old # new green function
  if is_sparse: 
    from scipy.sparse import csc_matrix
    g = csc_matrix(g)
  return g











def dos_infinite(intra,inter,energies=[0.0],num_rep=100,
                      mixing=0.7,eps=0.0001,green_guess=None,max_error=0.0001):
   """ Calculates the surface density of states by using a 
    green function approach"""
   dos = [] # list with the density of states
   iden = np.matrix(np.identity(len(intra),dtype=complex)) # create idntity
   for energy in energies: # loop over energies
     # right green function
     gr = dyson(intra,inter,energy=energy,num_rep=num_rep,mixing=mixing,
          eps=eps,green_guess=green_guess,max_error=max_error)
     # left green function
     gl = dyson(intra,inter.H,energy=energy,num_rep=num_rep,mixing=mixing,
          eps=eps,green_guess=green_guess,max_error=max_error)
     # central green function
     selfl = inter.H*gl*inter # left selfenergy
     selfr = inter*gr*inter.H # right selfenergy
     gc = energy*iden -intra -selfl -selfr # dyson equation for the center
     gc = gc.I # calculate inverse
     dos.append(-gc.trace()[0,0].imag)  # calculate the trace of the Green function
   return dos




def dos_semiinfinite(intra,inter,energies=[0.0],num_rep=100,
                      mixing=0.7,eps=0.0001,green_guess=None,max_error=0.0001):
   """ Calculates the surface density of states by using a 
    green function approach"""
   dos = [] # list with the density of states
   for energy in energies: # loop over energies
     gf = dyson(intra,inter,energy=energy,num_rep=num_rep,mixing=mixing,
          eps=eps,green_guess=green_guess,max_error=max_error)
     dos.append(-gf.trace()[0,0].imag)  # calculate the trace of the Green function
   return dos







def plot_dos_semiinfinite(intra,inter,energies=[0.0],num_rep=100,
                      mixing=0.7,eps=0.0001,green_guess=None,max_error=0.0001):
   """ Plots the surface density of states by using a 
    green function approach"""
   # get the dos
   dos = dos_semiinfinite(intra,inter,energies=energies,
             num_rep=num_rep,mixing=mixing,
             eps=eps,green_guess=green_guess,max_error=max_error)
   # plot the figure
   fig = py.figure() # create figure
   fig.subplots_adjust(0.2,0.2)
   fig.set_facecolor("white") # face in white
   sdos = fig.add_subplot(111) # create subplot
   sdos.set_xlabel("Energy",size=20)
   sdos.set_ylabel("Surface DOS",size=20)
   sdos.plot(energies,dos,color="red") # create the plot
   sdos.plot(energies,dos,color="red") # create the plot
   sdos.fill_between(energies,0,dos,color="red")
   sdos.tick_params(labelsize=20)
   sdos.set_ylim([0.0,max(dos)])
   return fig



def plot_dos_infinite(intra,inter,energies=[0.0],num_rep=100,
                      mixing=0.7,eps=0.0001,green_guess=None,max_error=0.0001):
   """ Plots the density of states by using a 
    green function approach"""
   # get the dos
   dos = dos_infinite(intra,inter,energies=energies,
             num_rep=num_rep,mixing=mixing,
             eps=eps,green_guess=green_guess,max_error=max_error)
   # plot the figure
   fig = py.figure() # create figure
   fig.set_facecolor("white") # face in white
   sp = fig.add_subplot(111) # create subplot
   sp.set_xlabel("Energy",size=20)
   sp.set_ylabel("Surface DOS",size=20)
   sp.plot(energies,dos) # create the plot
   return fig






def dos_heterostructure(hetero,energies=[0.0],num_rep=100,
                      mixing=0.7,eps=0.0001,green_guess=None,max_error=0.0001):
   """ Calculates the density of states 
       of a heterostructure by a  
    green function approach, input is a heterostructure class"""
   dos = [] # list with the density of states
   iden = np.matrix(np.identity(len(intra),dtype=complex)) # create idntity
   for energy in energies: # loop over energies
     # right green function
     intra = hetero.right_intra
     inter = hetero.right_inter
     gr = dyson(intra,inter,energy=energy,num_rep=num_rep,mixing=mixing,
          eps=eps,green_guess=green_guess,max_error=max_error)
     # left green function
     intra = hetero.right_intra
     inter = hetero.right_inter
     gl = dyson(intra,inter,energy=energy,num_rep=num_rep,mixing=mixing,
          eps=eps,green_guess=green_guess,max_error=max_error)
     # central green function
     selfl = inter.H*gl*inter # left selfenergy
     selfr = inter*gr*inter.H # right selfenergy
     gc = energy*iden -intra -selfl -selfr # dyson equation for the center
     gc = gc.I # calculate inverse
     dos.append(-gc.trace()[0,0].imag)  # calculate the trace of the Green function
   return dos



def read_matrix(f):
  """Read green function from a file"""
  m = np.genfromtxt(f)
  d = int(max(m.transpose()[0]))+1 # dimension of the green functions
  print d
  g = np.matrix([[0.0j for i in range(d)] for j in range(d)]) # create matrix
  for r in m:
    i = int(r[0])
    j = int(r[1])
    ar = r[2]
    ai = r[3]
    g[i,j] = ar +1j*ai # store element
  return g # return green function



def write_matrix(f,g):
  """Read green function from a file"""
  fw = open(f,"w") # open file to write
  n = len(g) # dimension of the matrix
  for i in range(n):
    for j in range(n):
      fw.write(str(i)+"  ")
      fw.write(str(j)+"  ")
      fw.write(str(g[i,j].real)+"  ")
      fw.write(str(g[i,j].imag)+"\n")
  fw.close()   # close file




def write_sparse(f,g):
  """ Write a sparse matrix in a file"""
  from input_tb90 import nv_el
  fw = open(f,"w") # open the file
  fw.write("# dimension = "+str(g.shape[0])+"\n")
  nv=nv_el(g)
  for iv in range(len(nv)):
    fw.write(str(int(nv[iv][0]))+'   ')
    fw.write(str(int(nv[iv][1]))+'   ')
    fw.write('{0:.8f}'.format(float(nv[iv][2]))+'   ')
    fw.write('{0:.8f}'.format(float(nv[iv][3]))+'   ')
    fw.write('  !!!  i  j   Real   Imag\n')
  fw.close()




def read_sparse(f,sparse=True):
  """Read green function from a file"""
  l = open(f,"r").readlines()[0] # first line
  d = int(l.split("=")[1])
  m = np.genfromtxt(f)
  if not sparse:
# create matrix  
    g = np.matrix([[0.0j for i in range(d)] for j in range(d)]) 
    for r in m:
      i = int(r[0])-1
      j = int(r[1])-1
      ar = r[2]
      ai = r[3]
      g[i,j] = ar +1j*ai # store element
  if sparse:
    from scipy.sparse import coo_matrix
    g = coo_matrix([[0.0j for i in range(d)] for j in range(d)]) 
    row = np.array([0 for i in range(len(m))])
    col = np.array([0 for i in range(len(m))])
    data = np.array([0j for i in range(len(m))])
    for i in range(len(m)):
      r = m[i]
      row[i] = int(r[0])-1
      col[i] = int(r[1])-1
      ar = r[2]
      ai = r[3]
      data[i] = ar +1j*ai # store element
    g.col = col
    g.row = row
    g.data = data
  return g # return green function





def gauss_inverse(m,i=0,j=0):
  from gauss_inv import gauss_inv as ginv
  """ Calculates the inverso of a block diagonal
      matrix """
  nb = len(m) # number of blocks
  ca = [None for ii in range(nb)]
  ua = [None for ii in range(nb-1)]
  da = [None for ii in range(nb-1)]
  for ii in range(nb): # diagonal part
    ca[ii] = m[ii][ii]
  for ii in range(nb-1):
    ua[ii] = m[ii][ii+1]
    da[ii] = m[ii+1][ii]
  mout = ginv(ca,da,ua,i+1,j+1)
  return np.matrix(mout)



