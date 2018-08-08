from __future__ import print_function
import geometry  # library to create crystal geometries
import numpy as np
import heterostructures
import matplotlib.pyplot as plt



def get_bar(delta1=0.0,delta2=0.0,phi=0.0,j=0.0,cou=1.0):
  g = geometry.square_ribbon(4) # create geometry of the system
  #g = geometry.honeycomb_zigzag_ribbon(1) # create geometry of the system
  g = geometry.chain() # create geometry of the system
  g.r = np.array([g.r[0]])
  g.a1 /= 2
  g.r2xyz()
#  g = g.supercell(4)
  h = g.get_hamiltonian() # create hamiltonian
  h.shift_fermi(1.0)
#  h.get_bands()
#  exit()
  hr = h.copy()
  hl = h.copy()
  hc = h.copy()
  hc.add_zeeman([0.,0.,j])
#  hc.add_rashba(0.2)
  # fermi and pairing 
#  hr.shift_fermi(1.)
#  hl.shift_fermi(1.)
#  hc.shift_fermi(1.)
  hr.add_swave(delta=delta2)
  hc.add_swave(delta=0.0)
  hl.add_swave(delta=delta1,phi=phi)
  
  
  
                                  # of the scattering centrl part
  # create a junction object
  ht = heterostructures.create_leads_and_central(hr,hl,hc,block_diagonal=False,
                                                    num_central = 1) 
#  hlist = [hc for i in range(80)]  # create a list with the hamiltonians 
  hlist = [hc]  # create a list with the hamiltonians 
#  ht = heterostructures.create_leads_and_central_list(hr,hl,hlist)
#  ht.left_coupling *= .2
  ht.right_coupling *= cou
  return ht




ht = get_bar(delta1=0.3,delta2=0.3,phi=0.0,j=1.2) # get the heterostructure

ht.delta = 0.01
#ht.setup_selfenergy_interpolation(delta=delta,pristine=True,
#                    es=np.linspace(-10.,10.,1000)) # create the functions

import heterostructures
es = np.linspace(-.6,.6,100) 
dacu = es*0.
if False:
  ds = heterostructures.central_dos(ht,energies=es)
  np.savetxt("DOS.OUT",np.matrix([es,ds]).T)
  exit()
fo = open("DOS_MAP.OUT","w")
for p in np.linspace(0.,2.,40): # loop
  ht = get_bar(delta1=0.3,delta2=0.1,phi=p,j=1.3,cou=0.1) # get the heterostructure
  ht.delta = 0.01
  ds = heterostructures.central_dos(ht,energies=es)
  dacu += np.array(ds)/40 # add
  for (e,d) in zip(es,ds): # loop
    fo.write(str(p)+"   "+str(e)+"    "+str(d)+"\n") # write parameter
  print("Done",p)
fo.close()

np.savetxt("SUMMED_DOS.OUT",np.matrix([es,dacu]).T)

#np.savetxt("DOS.OUT",np.matrix([es,ds]).T)
