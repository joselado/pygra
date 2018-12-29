# Add the root path of the pygra library
import os ; import sys ; sys.path.append(os.environ['PYGRAROOT'])

# zigzag ribbon
import numpy as np
from pygra importgeometry
from pygra importscftypes
import operators
from scipy.sparse import csc_matrix
g = geometry.honeycomb_lattice()
#g = geometry.square_lattice()
#g = geometry.triangular_lattice()
#g = geometry.chain()
#g = g.supercell(50)
g.write()
h = g.get_hamiltonian() # create hamiltonian of the system
h = h.get_multicell()
#h.remove_spin()
h.shift_fermi(0.6)
h.add_rashba(.3)
h.add_swave(0.0)
#h.get_bands()
#exit()
mf = scftypes.guess(h,mode="swave",fun=0.02)
#h.remove_spin()
mode = {"U":-10}
#mode = {"V":-3.}
#exit()
#h.turn_sparse()
scf = scftypes.selfconsistency(h,nkp=10,g=-10.0,
              mix=0.9,mf=mf,mode=mode)
              
#h = scf.hamiltonian
h.get_bands(nkpoints=500)
#exit()
from pygra importkdos
#kdos.write_surface(h)
#exit()                                             
#h = scf.hamiltonian
#h.check()
#exit()
import spectrum
#spectrum.fermi_surface(h)
