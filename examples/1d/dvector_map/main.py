# Add the root path of the pygra library
import os ; import sys 
sys.path.append(os.path.dirname(os.path.realpath(__file__))+"/../../../src")


import numpy as np
from pygra import geometry,meanfield
g = geometry.chain()
ns = 2 # make a supercell
g = g.supercell(ns)
h = g.get_hamiltonian() # create hamiltonian of the system
J = np.random.random(3) - 0.5 ; J = J/np.sqrt(J.dot(J)) # random vector
h.add_zeeman(J) # add magnetization in a random direction
h.setup_nambu_spinor() # tell the code to account for potential SC
scf = meanfield.Vinteraction(h,V1=-1.0,nk=10,filling=1./3.,mf="random",
    verbose=1 # to print how the scf progresses
    )
h = scf.hamiltonian # get the selfconssitent Hamiltonian
# write selfconsistent magnetization in MAGNETISM.OUT
scf.hamiltonian.write_magnetization(nrep=2) 
# write non-unitarity of the d-vector in NON_UNITARITY_MAP.OUT
scf.hamiltonian.write_non_unitarity(nrep=2) 
