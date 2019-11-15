# Add the root path of the pygra library
import os ; import sys ; sys.path.append(os.environ['PYGRAROOT'])

# zigzag ribbon
import numpy as np
from pygra import geometry
from pygra import scftypes
g = geometry.honeycomb_lattice()
h = g.get_hamiltonian() # create hamiltonian of the system
h = h.get_multicell()
h.shift_fermi(0.6)
h.add_swave(0.0)
mf = scftypes.guess(h,mode="swave",fun=0.02)
mode = {"U":-2}
from pygra import algebra
algebra.accelerate = True
scf = scftypes.selfconsistency(h,nkp=5,
              mix=0.9,mf=None,mode=mode)
             
h = scf.hamiltonian
print(h.extract("swave"))
h.write_swave()
#scf.hamiltonian.get_bands(operator="electron")

