# Add the root path of the pygra library
import os ; import sys ; sys.path.append(os.environ['PYGRAROOT'])

import numpy as np
from pygra import geometry
from pygra import spectrum
g = geometry.honeycomb_lattice()
h = g.get_hamiltonian(has_spin=True)
#h.get_qpi(delta=5e-2)
spectrum.multi_fermi_surface(h,nk=60,energies=np.linspace(-4,4,100),
        delta=0.1,nsuper=1)
