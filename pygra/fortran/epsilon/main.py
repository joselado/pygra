#import pyximport; pyximport.install()
import chi # library for response calculation
import geometry
import hamiltonians
import interactions
import numpy as np
import pylab as py

U = 1.0 # hubbard strength

g = geometry.chain()
g = geometry.honeycomb_zigzag_ribbon(1)
h = g.get_hamiltonian()

############# SCF
ab = interactions.hubbard(h,U=U) # create operators
mf = interactions.antiferro_initialization(h,value=0.1) # create operators
#mf = interactions.selfconsistency(h,ab_list=ab,old_mf=mf) # SCF cycle
mf = interactions.tb90_scf(h,ab,mf) # SCF cycle
#exit()

##############

h.intra += mf # add mean field

h.get_bands()
#exit()

#ms = chi.chi1d(h,energies=energies,q=0.1,U=U,adaptive=True,delta=delta,nk=100)
#exit()
#h.plot_bands()
#py.show()
#exit()

import time

energies = np.linspace(-.3,.3,100)
delta = 0.01
if True:
  #h.add_antiferromagnetism(.1)
  ks = np.linspace(.0,.1,100)
  fo = open("CHI2D.OUT","w")
  told = time.clock()
  for q in ks:
    told = time.clock()
    ms = chi.collinear_chi1d(h,energies=energies,q=q,U=U,adaptive=False,delta=delta,nk=600)
#    print "Coll",told - time.clock()
#    told = time.clock()
#    ms = chi.chi1d(h,energies=energies,q=q,U=U,adaptive=False,delta=delta,nk=100)
#    ms = chi.collinear_chi1d(h,energies=energies,q=q,U=U,adaptive=True,delta=delta,nk=100)
#    print "Nonoll",told - time.clock()
    told = time.clock()
    ms = chi.sumchi(ms) # sum all the elements
#    ms = energies*ms
    for (ei,mi) in zip(energies,ms):
      fo.write(str(q)+"    "+str(ei)+"    "+str(mi.imag)+"\n")
    print "Done",q
  fo.close()
  exit()
#####################
#####################
else:  # compare both schemes
  told = time.clock() # current time
  ms1 = chi.collinear_chi1d(h,energies=energies,q=.002,U=U,adaptive=False,delta=delta,nk=1000)
  ms1 = np.array([np.sum(mi) for mi in ms1])
  print "Coll",time.clock()-told
  told = time.clock()
#  ms = chi.chi1d(h,energies=energies,q=.002,U=U,adaptive=False,delta=delta)
  ms = chi.collinear_chi1d(h,energies=energies,q=.002,U=U,adaptive=True,delta=delta)
  print "Nonoll",time.clock()-told
  ms = np.array([np.sum(mi) for mi in ms])
  print "Difference",np.sum(np.abs(ms1-ms))
  import pylab as py
  py.plot(energies,-energies*ms1.imag)
  py.plot(energies,-energies*ms.imag)
#  py.plot(energies,ms.real)
  py.show()
