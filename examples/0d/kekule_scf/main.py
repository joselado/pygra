# Add the root path of the pygra library
import os ; import sys ; sys.path.append(os.environ['PYGRAROOT'])

import numpy as np
from pygra import geometry
from pygra import scftypes
g = geometry.honeycomb_lattice()
#g = geometry.chain()
g = g.supercell(6)
h = g.get_hamiltonian() # create hamiltonian of the system
h = h.get_multicell()
h.remove_spin()
h.turn_dense()

v = h.get_hopping_dict()
for key in v: v[key] *= 4.0

def callback_mf(mf):
    n = mf[(0,0,0)].shape[0]
    for i in range(n): mf[(0,0,0)][i,i] = 0.0
    return mf

scf = scftypes.densitydensity(h,nk=1,filling=0.5,v=v,callback_mf=callback_mf)
h = scf.hamiltonian # get the Hamiltonian
from pygra import groundstate
#exit()
#h = h.supercell(3)
groundstate.hopping(h) # write three replicas
#spectrum.fermi_surface(h)
