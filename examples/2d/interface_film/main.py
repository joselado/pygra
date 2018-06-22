import sys
sys.path.append("../../../pygra")  # add pygra library

import geometry
import hybrid
import films


# This script creates an interface between honeycomb AF and SC,
# showing a set of gap-less interface states

g = geometry.diamond_lattice() # diamond lattice

h = g.get_hamiltonian() # create hamiltonian of the system
#h.add_kane_mele(0.04)
h = films.build(h,nz=10)


h1 = h.copy() # copy Hamiltonian
h2 = h.copy() # copy Hamiltonian

h1.add_antiferromagnetism(0.5) # add antiferromagnetism


h1.add_swave(0.0) # add electron-hole


h2.shift_fermi(.4) # dope the system
h2.add_swave(0.5) # add swave paring


h = hybrid.half_and_half(h1,h2,tlen=.001,direction=2) # create a ribbon with half h1 and half h2

import topology

#topology.chern(h,nk=20) # write the Chern number
h.get_bands() # calculate band structure
