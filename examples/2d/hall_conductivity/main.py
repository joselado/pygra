# Add the root path of the pygra library
import os ; import sys 
sys.path.append(os.path.dirname(os.path.realpath(__file__))+"/../../../src")





from pygra import geometry
from pygra import topology
import numpy as np
mus = np.linspace(-0.7,0.7,40)
fo = open("HALL.OUT","w")
for mu in mus:
  g = geometry.honeycomb_lattice()
  h = g.get_hamiltonian(has_spin=True)
  h.add_zeeman([0.,0.,0.2]) # add exchange
  h.add_rashba(0.2) # add rashba SOC
  h.shift_fermi(mu)
  sigmaxy = topology.hall_conductivity(h,nk=20) # get
  print(mu,sigmaxy)
  fo.write(str(mu)+"  "+str(sigmaxy)+"\n")
fo.close()






