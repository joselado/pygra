# Add the root path of the pygra library
import os ; import sys ; sys.path.append(os.environ['PYGRAROOT'])

from pygra import geometry
from pygra import hamiltonians
import numpy as np
from pygra import specialhamiltonian
from pygra import parallel
from pygra import spectrum
parallel.cores = 7

h = specialhamiltonian.tbg(n=7,ti=0.4,is_sparse=True,has_spin=False)
h.set_filling(0.5,nk=2)
#h.get_bands(num_bands=20)
#exit()
spectrum.multi_fermi_surface(h,nk=60,energies=np.linspace(-0.05,0.05,100),
        delta=0.0005,nsuper=1)
