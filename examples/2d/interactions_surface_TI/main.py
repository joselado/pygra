# Add the root path of the pygra library
import os ; import sys 
sys.path.append(os.path.dirname(os.path.realpath(__file__))+"/../../../src")





# zigzag ribbon
from pygra importgeometry
from pygra importgeometry
g = geometry.single_square_lattice() # create the basic geometry
h = geometry2hamiltonian(g,mw=0.0) # get the Hamiltonian, mw is the Wilson mass
from pygra importscftypes
scf = scftypes.hubbardscf(h,U=1.,nkp=10,filling=0.5)
h = scf.hamiltonian
h.get_bands() # get the bandstructure
h.write()






