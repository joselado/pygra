# library to deal with the spectral properties of the hamiltonian
import numpy as np
import scipy.linalg as lg

def fermi_surface(h,write=True,output_file="FERMI_MAP.OUT",
                    e=0.0,nk=50,nsuper=1,reciprocal=False,
                    delta=None,refine_delta=1.0,operator=None):
  """Calculates the Fermi surface of a 2d system"""
  if h.dimensionality!=2: raise  # continue if two dimensional
  hk_gen = h.get_hk_gen() # gets the function to generate h(k)
  kxs = np.linspace(-nsuper,nsuper,nk)  # generate kx
  kys = np.linspace(-nsuper,nsuper,nk)  # generate ky
  iden = np.identity(h.intra.shape[0],dtype=np.complex)
  kdos = [] # empty list
  kxout = []
  kyout = []
  if reciprocal: R = h.geometry.get_k2K() # get matrix
  else:  R = np.matrix(np.identity(3)) # get identity
  # setup a reasonable value for delta
  if delta is None:
    delta = 1./refine_delta*2.*np.max(np.abs(h.intra))/nk
  # setup the operator
  if operator is None:
    operator = np.matrix(np.identity(h.intra.shape[0]))
  for x in kxs:
    for y in kxs:
      r = np.matrix([x,y,0.]).T # real space vectors
      k = np.array((R*r).T)[0] # change of basis
      hk = hk_gen(k) # get hamiltonian
      gf = ((e+1j*delta)*iden - hk).I # get green function
      if callable(operator):
        tdos = -(operator(x,y)*gf).imag # get imaginary part
      else: tdos = -(operator*gf).imag # get imaginary part
      kdos.append(tdos.trace()[0,0]) # add to the list
#      kdos.append(np.sum([tdos[i,i]*(-1)**i for i in range(tdos.shape[0])])) # add to the list
      kxout.append(x)
      kyout.append(y)
  if write:  # optionally, write in file
    f = open(output_file,"w") 
    for (x,y,d) in zip(kxout,kyout,kdos):
      f.write(str(x)+ "   "+str(y)+"   "+str(d)+"\n")
    f.close() # close the file
  return (kxout,kyout,d) # return result

