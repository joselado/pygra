# Add the root path of the pygra library
import os ; import sys ; sys.path.append(os.environ['PYGRAROOT'])

from pygra import specialhamiltonian
h = specialhamiltonian.valence_TMDC(soc=0.1)
h = h.supercell(3)
h.write_hopping()
h.get_bands()
