import green
import numpy as np

def dos_surface(h,output_file="DOS.OUT",
                 energies=np.linspace(-1.,1.,20),delta=0.001):
  """Calculates the DOS of a surface, and writes in file"""
  if h.dimensionality!=1: raise # only for 1d
  fo = open(output_file,"w")
  fo.write("# energy, DOS surface, DOS bulk\n")
  for e in energies: # loop over energies
    print "Done",e
    gb,gs = green.green_renormalization(h.intra,h.inter,energy=e,delta=delta)
    gb = -gb.trace()[0,0].imag
    gs = -gs.trace()[0,0].imag
    fo.write(str(e)+"     "+str(gs)+"    "+str(gb)+"\n")
  fo.close()




def dos0d(h,es=[],delta=0.001):
  """Calculate density of states of a 0d system"""
  ds = [] # empty list
  if h.dimensionality==0:  # only for 0d
    iden = np.identity(h.intra.shape[0],dtype=np.complex) # create identity
    for e in es: # loop over energies
      g = ( (e+1j*delta)*iden -h.intra ).I # calculate green function
      ds.append(-g.trace()[0,0].imag)  # add this dos
  else: raise # not implemented...
  write_dos(es,ds)
  return ds





def dos0d_kpm(h,use_kpm=True,scale=10,npol=100,ntries=100):
  """ Calculate density of states of a 1d system"""
  if h.dimensionality!=0: raise # only for 0d
  if not use_kpm: raise # only using KPM
  h.turn_sparse() # turn the hamiltonian sparse
  mus = np.array([0.0j for i in range(2*npol)]) # initialize polynomials
  import kpm
  mus = kpm.random_trace(h.intra/scale,ntries=ntries,n=npol)
  xs = np.linspace(-0.9,0.9,4*npol) # x points
  ys = kpm.generate_profile(mus,xs) # generate the profile
  write_dos(xs*scale,ys) # write in file


def dos0d_sites(h,sites=[0],scale=10.,npol=100,ewindow=None,refine_e=1.0):
  """ Calculate density of states of a 1d system for a certain orbitals"""
  if h.dimensionality!=0: raise # only for 1d
  h.turn_sparse() # turn the hamiltonian sparse
  mus = np.array([0.0j for i in range(2*npol)]) # initialize polynomials
  import kpm
  hk = h.intra # hamiltonian
  for isite in sites:
    mus += kpm.local_dos(hk/scale,i=isite,n=npol)
  if ewindow is None:  xs = np.linspace(-0.9,0.9,int(npol*refine_e)) # x points
  else:  xs = np.linspace(-ewindow/scale,ewindow/scale,npol) # x points
  ys = kpm.generate_profile(mus,xs) # generate the profile
  write_dos(xs*scale,ys) # write in file











def write_dos(es,ds):
  """ Write DOS in a file"""
  f = open("DOS.OUT","w")
  for (e,d) in zip(es,ds):
    f.write(str(e)+"     ")
    f.write(str(d)+"\n")
  f.close()




def dos1d(h,use_kpm=True,scale=10.,nk=100,npol=100,ntries=100):
  """ Calculate density of states of a 1d system"""
  if h.dimensionality!=1: raise # only for 1d
  if not use_kpm: raise # only using KPM
  ks = np.linspace(0.,1.,nk,endpoint=False) # number of kpoints
  h.turn_sparse() # turn the hamiltonian sparse
  hkgen = h.get_hk_gen() # get generator
  mus = np.array([0.0j for i in range(2*npol)]) # initialize polynomials
  import kpm
  for k in ks: # loop over kpoints
    hk = hkgen(k) # hamiltonian
    mus += kpm.random_trace(hk/scale,ntries=ntries,n=npol)
  mus /= nk # normalize by the number of kpoints
  xs = np.linspace(-0.9,0.9,4*npol) # x points
  ys = kpm.generate_profile(mus,xs) # generate the profile
  write_dos(xs*scale,ys) # write in file




def dos1d_sites(h,sites=[0],scale=10.,nk=100,npol=100,info=False,ewindow=None):
  """ Calculate density of states of a 1d system for a certain orbitals"""
  if h.dimensionality!=1: raise # only for 1d
  ks = np.linspace(0.,1.,nk,endpoint=False) # number of kpoints
  h.turn_sparse() # turn the hamiltonian sparse
  hkgen = h.get_hk_gen() # get generator
  mus = np.array([0.0j for i in range(2*npol)]) # initialize polynomials
  import kpm
  for k in ks: # loop over kpoints
    hk = hkgen(k) # hamiltonian
    for isite in sites:
      mus += kpm.local_dos(hk/scale,i=isite,n=npol)
    if info: print "Done",k
  mus /= nk # normalize by the number of kpoints
  if ewindow is None:  xs = np.linspace(-0.9,0.9,npol) # x points
  else:  xs = np.linspace(-ewindow/scale,ewindow/scale,npol) # x points
  ys = kpm.generate_profile(mus,xs) # generate the profile
  write_dos(xs*scale,ys) # write in file




def dos2d(h,use_kpm=True,scale=10.,nk=20,npol=100,ntries=100):
  """ Calculate density of states of a 1d system"""
  if h.dimensionality!=2: raise # only for 2d
  if not use_kpm: raise # only using KPM
  ks = []
  for ik in np.linspace(0.,1.,nk,endpoint=False):
    for jk in np.linspace(0.,1.,nk,endpoint=False):
      ks.append(np.array([ik,jk])) # add point
  h.turn_sparse() # turn the hamiltonian sparse
  hkgen = h.get_hk_gen() # get generator
  mus = np.array([0.0j for i in range(2*npol)]) # initialize polynomials
  import kpm
  for k in ks: # loop over kpoints
    hk = hkgen(k) # hamiltonian
    mus += kpm.random_trace(hk/scale,ntries=ntries,n=npol)
  mus /= len(ks) # normalize by the number of kpoints
  xs = np.linspace(-0.9,0.9,npol) # x points
  ys = kpm.generate_profile(mus,xs) # generate the profile
  write_dos(xs*scale,ys) # write in file


def dos2d_ewindow(h,energies=np.linspace(-1.,1.,30),delta=None,info=False,
                    use_green=True,nk=300):
  """Calculate the density of states in certain eenrgy window"""
  ys = [] # density of states
  if delta is None: # pick a good delta value
    delta = 0.1*(max(energies) - min(energies))/len(energies)
  if use_green:
    from green import bloch_selfenergy
    for energy in energies:
      (g,selfe) = bloch_selfenergy(h,nk=100,energy=energy, delta=delta,
                   mode="adaptive")
      ys.append(-g.trace()[0,0].imag)
      if info: print "Done",energy
    write_dos(energies,ys) # write in file
    return
  else: # do not use green function    
    from dosf90 import calculate_dos # import fortran library
    import scipy.linalg as lg
    kxs = np.linspace(0.,1.,nk)
    kys = np.linspace(0.,1.,nk)
    hkgen= h.get_hk_gen() # get hamiltonian generator
    ys = energies*0.
    weight = 1./(nk*nk)
    for ix in kxs:
      for iy in kys:
        k = np.array([ix,iy,0.]) # create kpoint
        hk = hkgen(k) # get hk hamiltonian
        evals = lg.eigvalsh(hk) # get eigenvalues
        ys += weight*calculate_dos(evals,energies,delta) # add this contribution
      if info: print "Done",ix
    write_dos(energies,ys) # write in file
    return






def dos1d_ewindow(h,energies=np.linspace(-1.,1.,30),delta=None,info=False,
                    use_green=True,nk=300):
  """Calculate the density of states in certain eenrgy window"""
  ys = [] # density of states
  if delta is None: # pick a good delta value
    delta = 0.1*(max(energies) - min(energies))/len(energies)
  if True: # do not use green function    
    from dosf90 import calculate_dos # import fortran library
    import scipy.linalg as lg
    kxs = np.linspace(0.,1.,nk)
    hkgen= h.get_hk_gen() # get hamiltonian generator
    ys = energies*0.
    weight = 1./(nk)
    for ix in kxs:
      hk = hkgen(ix) # get hk hamiltonian
      evals = lg.eigvalsh(hk) # get eigenvalues
      ys += weight*calculate_dos(evals,energies,delta) # add this contribution
    if info: print "Done",ix
    write_dos(energies,ys) # write in file
    return











def dos_ewindow(h,energies=np.linspace(-1.,1.,30),delta=None,info=False,
                    use_green=True,nk=300):
  """ Calculate density of states in an energy window"""
  if h.dimensionality==2: # two dimensional
    dos2d_ewindow(h,energies=energies,delta=delta,info=info,
                    use_green=use_green,nk=nk)
  elif h.dimensionality==1: # one dimensional
    dos1d_ewindow(h,energies=energies,delta=delta,info=info,
                    use_green=use_green,nk=nk)
  else: raise # not implemented
