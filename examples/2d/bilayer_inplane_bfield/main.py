# Add the root path of the pygra library
import os ; import sys ; sys.path.append(os.environ['PYGRAROOT'])
import numpy as np
from pygra import specialhamiltonian
h = specialhamiltonian.multilayer_graphene(l=[0,1],ti=0.0)
h = h.get_multicell()
h.add_inplane_bfield(b=0.1,phi=0.5)
print(h.intra)
h.get_bands()
from pygra import spectrum
spectrum.multi_fermi_surface(h,nk=60,energies=np.linspace(-4,4,100),
        delta=0.01,nsuper=1)

