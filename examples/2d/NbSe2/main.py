# Add the root path of the pygra library
import os ; import sys ; sys.path.append(os.environ['PYGRAROOT'])

from pygra import specialhamiltonian
from pygra import geometry
import numpy as np
g = geometry.triangular_lattice()
g = g.supercell(3)
#h = specialhamiltonian.valence_TMDC(soc=0.1,g=g)
h = specialhamiltonian.NbSe2(soc=0.3)
h.get_bands(operator="sz")
h.get_multi_fermi_surface(energies=np.linspace(-6.,6.,100),delta=3e-2)
