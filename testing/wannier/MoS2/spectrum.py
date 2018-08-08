# library to deal with the spectral properties of the hamiltonian
import numpy as np
import scipy.linalg as lg

def fermi_surface(h,nk,write=True,output_file="FERMI_SURFACE.OUT",
                    e=0.0,nk=10,
                    delta=0.01):
   """Calculates the Fermi surface of a 2d system"""
  if h.dimensionality==2: pass  # continue if two dimensional
  else: raise  # fail if not implemented

  hk_gen = h.get_hk_gen() # gets the function to generate h(k)
  kxs = np.linspace(0.,1.,nk)  # generate kx
  kys = np.linspace(0.,1.,nk)  # generate ky
  iden = np.identity(len(h.intra),dtype=np.complex)
  kdos = [] # empty list
  for x in kxs:
    for y in kxs:
      hk = hk_gen(np.array([x,y])) # get hamiltonian
      gf = ((e+1j*delta)*den - hk) # get green function
      kdos.append(-gf.trace()[0,0].imag) # add to the list
  if write:  # optionally, write in file
    f = open(output_file,"w") 
    for (x,y,d) in zip(kxs,kys,d):
      f.write(str(x)+ "   "+str(y)+"   "+str(d)+"\n")
    f.close() # close the file
  return (kxs,kys,d) # return result

