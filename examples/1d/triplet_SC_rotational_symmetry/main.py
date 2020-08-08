# Add the root path of the pygra library
import os ; import sys ; sys.path.append(os.environ['PYGRAROOT'])

import numpy as np
from pygra import geometry
from pygra import groundstate
from pygra import meanfield
from scipy.sparse import csc_matrix
g = geometry.chain()
#g = g.supercell(2)

def get():
    h = g.get_hamiltonian() # create hamiltonian of the system
    m = np.random.random(3)-0.5
    m = m/np.sqrt(m.dot(m)) # random magnetic field
    h.add_zeeman(m)
    nk = 30
    filling = 0.5
    h.turn_nambu()
    mf = meanfield.guess(h,"random")

    scf = meanfield.Vinteraction(h,V1=-2.0,nk=nk,filling=filling,mf=mf,
            constrains =["no_charge"],verbose=0)
    h = scf.hamiltonian # get the Hamiltonian
    return h.get_gap()


for i in range(3):
    print(get())


