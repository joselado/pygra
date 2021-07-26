# Add the root path of the pygra library
import os ; import sys 
sys.path.append(os.path.dirname(os.path.realpath(__file__))+"/../../../src")





from pygra importgeometry
import numpy as np
import topology
import klist
def geth(mu,delta=0.0):
  g = geometry.honeycomb_zigzag_ribbon(10)
  h = g.get_hamiltonian(has_spin=True)
  
  
  def fm(r):
      if r[1]<(np.min(g.y)+2.0): return [0.6,0.,0.]
      else: return [0.,0.,0.]
  
  
#  def fd(r):
#      if r[1]>0.0: return 0.1
#      else: return 0.0
#  def ff(r):
#      if r[1]>0.0: return mu
#      return 0.0
  
  
  h.add_zeeman(fm)
  h.add_kane_mele(0.02)
  h.shift_fermi(mu)
  h.add_swave(delta)
  return h
h = geth(0.0)
#h.get_bands(operator="sx")
#exit()
import green
es = np.linspace(-0.2,0.2,50)
#(xs,ys) = green.dos_semiinfinite(h.intra,h.inter,energies=es)
#np.savetxt("DOS.OUT",np.matrix([xs,ys]).T)
#exit()
mus = np.linspace(0.,0.5,40)
gs = []
nus = []
import topology
for mu in mus:
  h = geth(mu,delta=0.1)
  g = h.get_gap()
  nu = abs(topology.berry_phase(h,nk=10)/np.pi)
  nus.append(abs(nu))
  gs.append(g)
  print(mu,g,nu)
import matplotlib.pyplot as plt
plt.subplot(121)
plt.plot(mus,gs,marker="o")
plt.subplot(122)
plt.plot(mus,nus,marker="o")
plt.show()






