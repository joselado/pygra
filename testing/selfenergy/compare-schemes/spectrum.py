# library to deal with the spectral properties of the hamiltonian
import numpy as np
import scipy.linalg as lg
import os

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




def boolean_fermi_surface(h,write=True,output_file="BOOL_FERMI_MAP.OUT",
                    e=0.0,nk=50,nsuper=1,reciprocal=False,
                    delta=None):
  """Calculates the Fermi surface of a 2d system"""
  if h.dimensionality!=2: raise  # continue if two dimensional
  hk_gen = h.get_hk_gen() # gets the function to generate h(k)
  kxs = np.linspace(-nsuper,nsuper,nk)  # generate kx
  kys = np.linspace(-nsuper,nsuper,nk)  # generate ky
  kdos = [] # empty list
  kxout = []
  kyout = []
  if reciprocal: R = h.geometry.get_k2K() # get matrix
  # setup a reasonable value for delta
  if delta is None:
    delta = 8./np.max(np.abs(h.intra))/nk
  for x in kxs:
    for y in kxs:
      r = np.matrix([x,y,0.]).T # real space vectors
      k = np.array((R*r).T)[0] # change of basis
      hk = hk_gen(k) # get hamiltonian
      evals = lg.eigvalsh(hk) # diagonalize
      de = np.abs(evals - e) # difference with respect to fermi
      de = de[de<delta] # energies close to fermi
      if len(de)>0: kdos.append(1.0) # add to the list
      else: kdos.append(0.0) # add to the list
      kxout.append(x)
      kyout.append(y)
  if write:  # optionally, write in file
    f = open(output_file,"w") 
    for (x,y,d) in zip(kxout,kyout,kdos):
      f.write(str(x)+ "   "+str(y)+"   "+str(d)+"\n")
    f.close() # close the file
  return (kxout,kyout,d) # return result
























def get_bands(h,output_file="BANDS2D_",nindex=[-1,1],
               nk=50,nsuper=1,reciprocal=False,
               operator=None,k0=[0.,0.]):
  """ Calculate band structure"""
  if h.dimensionality!=2: raise  # continue if two dimensional
  hk_gen = h.get_hk_gen() # gets the function to generate h(k)
  kxs = np.linspace(-nsuper,nsuper,nk)+k0[0]  # generate kx
  kys = np.linspace(-nsuper,nsuper,nk)+k0[1]  # generate ky
  kdos = [] # empty list
  kxout = []
  kyout = []
  if reciprocal: R = h.geometry.get_k2K() # get matrix
  else:  R = np.matrix(np.identity(3)) # get identity
  # setup a reasonable value for delta
  # setup the operator
  if operator is None:
    operator = np.matrix(np.identity(h.intra.shape[0]))
  os.system("rm "+output_file+"*") # delete previous files
  for x in kxs:
    for y in kxs:
      r = np.matrix([x,y,0.]).T # real space vectors
      k = np.array((R*r).T)[0] # change of basis
      hk = hk_gen(k) # get hamiltonian
      evals = lg.eigvalsh(hk) # eigenvalues
      epos = sorted(evals[evals>0]) # positive energies
      eneg = sorted(np.abs(evals[evals<0])) # negative energies
      for i in nindex: # loop over bands
        fo = open(output_file+"_"+str(i)+".OUT","a")  # append        
        fo.write(str(x)+"     "+str(y)+"   ")
        if i>0: fo.write(str(epos[i-1])+"\n")
        if i<0: fo.write(str(-eneg[abs(i)-1])+"\n")
        fo.close() # close file





