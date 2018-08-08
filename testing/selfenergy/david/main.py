import geometry  # library to create crystal geometries
import hamiltonians  # library to work with hamiltonians
import numpy as np
import pylab as py
import green

##### Create the hamiltonian #######
g = geometry.honeycomb_lattice()  # create a honeycomb lattice
g = geometry.supercell2d(g,n1=1,n2=1)
h = hamiltonians.hamiltonian(g) # create hamiltonian
h.first_neighbors()  # create first neighbor hamiltonian
h.remove_spin()  # spinless hamiltonian
##### End create the hamiltonian #######


### now create arrays of energies and dos ####
es = np.linspace(-3.,3.,100)  # array with energies
dos = []  # arry with pristine DOS
dosv = []  # array with defected DOS
### end create arrays of energies and dos ####

#### and cell with the defect ####
vintra = h.intra.copy()   # hoppings intracell for the defected one
vintra[len(vintra)/2,len(vintra)/2] = 10000.  # model vacancy as huge onsite
#### end cell with the defect ####


### perform Green function calculation over the energies #####

for e in es:  # loop over energies
  delta = 0.02
  g,selfe = green.bloch_selfenergy(h,energy=e,delta=delta,nk=200,
                                     mode="renormalization")
  emat = np.matrix(np.identity(len(g)))*(e + delta*1j)  # E +i\delta 
  gv = (emat - vintra -selfe).I   # Green function of a vacancy, with selfener
  dos.append(-g.trace()[0,0].imag)  # save DOS of the pristine
  dosv.append(-gv.trace()[0,0].imag)  # save DOS of the defected

### end Green function calculation over the energies #####



#### finally plot  ####
py.plot(es,dos,marker="o",color="red",label="pristine")
py.plot(es,dosv,marker="o",color="blue",label="defected")
py.legend()

py.show()

#### end plot  ####
