from __future__ import print_function
import geometry  # library to create crystal geometries
import numpy as np
import heterostructures
import matplotlib.pyplot as plt



def get_bar(param):
  g = geometry.square_ribbon(4) # create geometry of the system
  #g = geometry.honeycomb_zigzag_ribbon(1) # create geometry of the system
  g = geometry.chain() # create geometry of the system
  g.r = np.array([g.r[0]])
  g.a1 /= 2
  g.r2xyz()
#  g = g.supercell(4)
  h = g.get_hamiltonian() # create hamiltonian
#  h.get_bands()
#  exit()
  hr = h.copy()
  hl = h.copy()
  hc = h.copy()
  
  # fermi and pairing 
  hr.shift_fermi(1.)
  hl.shift_fermi(1.)
  hc.shift_fermi(1.)
  hr.add_swave(param)
  hc.add_swave(0.0)
  hl.add_swave(0.0)
  
  
  
                                  # of the scattering centrl part
  # create a junction object
  ht = heterostructures.create_leads_and_central(hr,hl,hc,block_diagonal=False,
                                                    num_central = 1) 
#  hlist = [hc for i in range(80)]  # create a list with the hamiltonians 
  hlist = [hc]  # create a list with the hamiltonians 
#  ht = heterostructures.create_leads_and_central_list(hr,hl,hlist)
#  ht.left_coupling *= .2
  ht.right_coupling *= .1
  return ht




ht = get_bar(0.3) # get the heterostructure

delta = 0.01
ht.setup_selfenergy_interpolation(delta=delta,pristine=True,
                    es=np.linspace(-10.,10.,1000)) # create the functions
import keldysh
import os
os.system("rm TEST_*") # remove files

vs = np.linspace(0.2,0.5,10)
if True:
  fo = open("I_VS_V.OUT","w")
  for v in vs:
  #  ii = keldysh.calculate_current(ht,v=v,delta=0.01)
    ii = ht.didv(v,delta=delta)
    print("Current",ii)
    fo.write(str(v)+"   "+str(ii)+"\n")
    fo.flush()
  fo.close()
else:
  import parallel
  def f(v):
    return keldysh.calculate_current(ht,v=v,delta=delta)
  iis = parallel.pcall(f,vs) # get currents
  didv = np.gradient(np.array(iis))/(vs[1]-vs[0])
  np.savetxt("I_VS_V.OUT",np.matrix([vs,didv,iis]).T)


