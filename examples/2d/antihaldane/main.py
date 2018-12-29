# Add the root path of the pygra library
import os ; import sys ; sys.path.append(os.environ['PYGRAROOT'])

from pygra import geometry
g = geometry.honeycomb_lattice()
h = g.get_hamiltonian(has_spin=True)
#h.clean()
#h.add_zeeman(0.2)
h.add_antihaldane(0.1)
#h.add_swave(0.1)
h.get_bands(operator=h.get_operator("sz"))
#h.get_bands(operator=h.get_operator("valley"))
