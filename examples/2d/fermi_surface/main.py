# Add the root path of the pygra library
import os ; import sys 
sys.path.append(os.path.dirname(os.path.realpath(__file__))+"/../../../src")





from pygra import geometry
from pygra import topology
from pygra import spectrum
g = geometry.honeycomb_lattice()
h = g.get_hamiltonian(has_spin=True)
h.add_onsite(0.6)
h.get_bands()
spectrum.fermi_surface(h)






