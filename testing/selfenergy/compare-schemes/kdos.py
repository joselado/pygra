import numpy as np
import green

def write_kdos(k=0.,es=[],ds=[],new=True):
  """ Write KDOS in a file"""
  if new: f = open("KDOS.OUT","w") # open new file
  else: f = open("KDOS.OUT","a") # continue writting
  for (e,d) in zip(es,ds): # loop over e and dos
    f.write(str(k)+"     ")
    f.write(str(e)+"     ")
    f.write(str(d)+"\n")
  f.close()





def kdos1d_sites(h,sites=[0],scale=10.,nk=100,npol=100,kshift=0.,
                  ewindow=None,info=False):
  """ Calculate kresolved density of states of
  a 1d system for a certain orbitals"""
  if h.dimensionality!=1: raise # only for 1d
  ks = np.linspace(0.,1.,nk) # number of kpoints
  h.turn_sparse() # turn the hamiltonian sparse
  hkgen = h.get_hk_gen() # get generator
  if ewindow is None:  xs = np.linspace(-0.9,0.9,nk) # x points
  else:  xs = np.linspace(-ewindow/scale,ewindow/scale,nk) # x points
  import kpm
  write_kdos() # initialize file
  for k in ks: # loop over kpoints
    mus = np.array([0.0j for i in range(2*npol)]) # initialize polynomials
    hk = hkgen(k+kshift) # hamiltonian
    for isite in sites:
      mus += kpm.local_dos(hk/scale,i=isite,n=npol)
    ys = kpm.generate_profile(mus,xs) # generate the profile
    write_kdos(k,xs*scale,ys,new=False) # write in file (append)
    if info: print("Done",k)


def surface(h,energies=None,klist=None,delta=0.01):
  bout = [] # empty list, bulk
  sout = [] # empty list, surface
  for k in klist:
    for energy in energies:
      gs,sf = green.green_kchain(h,k=k,energy=energy,delta=delta,only_bulk=False) 
      bout.append(gs.trace()[0,0].imag) # bulk
      sout.append(sf.trace()[0,0].imag) # surface
  bout = np.array(bout).reshape((len(energies),len(klist))) # convert to array
  sout = np.array(sout).reshape((len(energies),len(klist))) # convert to array
  return (bout.transpose(),sout.transpose())




def write_surface(h,energies=None,klist=None,delta=0.01):
  bout = [] # empty list, bulk
  sout = [] # empty list, surface
  if klist is None: klist = np.linspace(-.5,.5,50)
  if energies is None: klist = np.linspace(-.5,.5,50)
  fo  = open("KDOS.OUT","w") # open file
  for k in klist:
    for energy in energies:
      gs,sf = green.green_kchain(h,k=k,energy=energy,delta=delta,only_bulk=False) 
      db = -gs.trace()[0,0].imag # bulk
      ds = -sf.trace()[0,0].imag # surface
      fo.write(str(k)+"   "+str(energy)+"   "+str(ds)+"   "+str(db)+"\n")
  fo.close()

