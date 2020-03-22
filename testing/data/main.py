import geometry  # library to create crystal geometries
import hamiltonians  # library to work with hamiltonians
import numpy as np



ncell = 15 # number of supercells

g = geometry.honeycomb_lattice()  # create a honeycomb lattice

h2 = g.get_hamiltonian() # create hamiltonian
g = g.supercell(ncell) # create a supercell
h1 = g.get_hamiltonian() # create hamiltonian
h1.add_rashba(.1)
h2.add_rashba(.1)

h1.write(output_file="h1.in")
h2.write(output_file="h2.in")

#### Parameters ####
delta = 0.02 # analitic continuation
e = 0.7 # energy



## Calculate by both methods
import green
import time

t0 = time.perf_counter()
### OLD METHOD ###
g1,selfe1 = green.bloch_selfenergy(h1,energy=e,delta=delta,nk=200,
                                     mode="adaptative")


t1 = time.perf_counter()
### NEW METHOD ###

g2,selfe2 = green.supercell_selfenergy(h2,e=e,delta=delta,nk=300,nsuper=ncell)


t2 = time.perf_counter()

## Output results

print "Time for OLD = ",t1-t0
print "Time for NEW = ",t2-t1

print "Error in bulk green = ",np.max(np.abs(g1-g2))
print "Error in selfenergy = ",np.max(np.abs(selfe1-selfe2))
