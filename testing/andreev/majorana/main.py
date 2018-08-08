import geometry  # library to create crystal geometries
import numpy as np
import heterostructures
import matplotlib.pyplot as plt

g = geometry.square_ribbon(4) # create geometry of the system
#g = geometry.honeycomb_zigzag_ribbon(1) # create geometry of the system
g = geometry.square_ribbon(1) # create geometry of the system
#g = g.supercell(10)
h = g.get_hamiltonian() # create hamiltonian
#h.shift_fermi(0.5)
hr = h.copy()
hl = h.copy()
hc = h.copy()

hc.add_rashba(.6)
hc.add_zeeman([.0,0.,0.2])
hc.shift_fermi(2.0)

#hc.get_bands()
#exit()

#exit()
#hr.shift_fermi(1.)
hr.add_swave(0.0)
hc.add_swave(0.1)
hl.add_swave(0.0)

hc.get_bands()

es = np.linspace(-.2,.2,100) # array with the energies

                                # of the scattering centrl part
# create a junction object
ht = heterostructures.create_leads_and_central(hr,hl,hc,block_diagonal=False,
                                                  num_central = 1) 
hlist = [hc for i in range(60)]  # create a list with the hamiltonians 
ht = heterostructures.create_leads_and_central_list(hr,hl,hlist)
ht.left_coupling *= .3
ht.right_coupling *= .3
gs = []
# calculate
G = heterostructures.didv(ht,energy = 0.4)
#exit()
for e in es:
  G = heterostructures.didv(ht,energy = e)
  gs.append(G)
  print G

plt.plot(es,gs)
plt.show()
