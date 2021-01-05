# Add the root path of the pygra library
import os ; import sys ; sys.path.append(os.environ['PYGRAROOT'])

from pygra import geometry,specialhamiltonian
h = specialhamiltonian.triangular_pi_flux(has_spin=False) # get the pi-flux hamiltonian
h.get_bands()
h.write_hopping()
