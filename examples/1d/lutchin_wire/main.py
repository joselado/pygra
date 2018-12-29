# Add the root path of the pygra library
import os ; import sys ; sys.path.append(os.environ['PYGRAROOT'])

from pygra import geometry
from pygra import topology
from pygra import operators
g = geometry.chain() # create geometry of a chain
h = g.get_hamiltonian(has_spin=True) # get the Hamiltonian, spinfull
h.add_rashba(0.5) # add Rashba SOC
h.add_zeeman(0.3) # add Zeeman field
h.shift_fermi(2.) # add Zeeman field
h.add_swave(0.2) # add swave pairing
h.get_bands(operator=operators.get_sy(h))
