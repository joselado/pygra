# Add the root path of the pygra library
import os ; import sys ; sys.path.append(os.environ['PYGRAROOT'])

# zigzag ribbon
from pygra import geometry
from pygra import scftypes
g = geometry.honeycomb_zigzag_ribbon(10) # create geometry of a zigzag ribbon
h = g.get_hamiltonian() # create hamiltonian of the system
mf = scftypes.guess(h,"ferro",fun=lambda r: [0.,0.,1.])
scf = scftypes.hubbardscf(h,nkp=30,filling=0.5,mf=mf)
h = scf.hamiltonian # get the Hamiltonian
h.get_bands(operator="sz") # calculate band structure
