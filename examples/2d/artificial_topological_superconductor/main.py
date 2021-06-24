# Add the root path of the pygra library
import os ; import sys ; sys.path.append(os.environ['PYGRAROOT'])

import numpy as np
from pygra import geometry
g = geometry.honeycomb_lattice() # geometry of a honeycomb lattice
h = g.get_hamiltonian(has_spin=True) # create hamiltonian of the system
h.shift_fermi(3.0) # bottom of the band
h.add_rashba(0.5) # add Rashba SOC
h.add_zeeman([0.,0.,0.5]) # add a Zeeman field
h.add_swave(0.1) # add s-wave superconductivity
c = h.get_chern(nk=20) # compute Chern number
print()
print("########################")
print("Chern number = ",round(c,2))
print("########################")
print()
h.get_bands(operator="sx") # compute band structure
