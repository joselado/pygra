# Add the root path of the pygra library
import os ; import sys ; sys.path.append(os.environ['PYGRAROOT'])

from pygra import islands
import numpy as np
g = islands.get_geometry(name="honeycomb",n=3,nedges=3,rot=0.0) # get an island
# maximum distance to the origin
h = g.get_hamiltonian(has_spin=True) # get the Hamiltonian
from pygra import meanfield
g.write()

mf = meanfield.guess(h,mode="ferro")
scf = meanfield.Vinteraction(h,filling=0.5,U=3.0,V1=1.0,mf=mf,maxerror=1e-9)
scf.hamiltonian.write_hopping(spin_imbalance=True)
scf.hamiltonian.write_magnetization()
#scf.hamiltonian.get_bands()
