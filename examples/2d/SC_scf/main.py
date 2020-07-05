# Add the root path of the pygra library
import os ; import sys ; sys.path.append(os.environ['PYGRAROOT'])

# zigzag ribbon
import numpy as np
from pygra import geometry
from pygra import scftypes
from pygra import meanfield
import os
g = geometry.honeycomb_lattice()
h0 = g.get_hamiltonian() # create hamiltonian of the system
ds = []
Us = np.linspace(0.0,3.0,10)
f = open("DELTA_VS_T_VS_MU.OUT","w")
h0.add_swave(0.0)
for U in Us:
    h = h0.copy()
    os.system("rm -rf *.pkl")
    #scf = scftypes.attractive_hubbard(h,nk=10,mix=0.9,mf=None,g=-2.0,T=t)
    mf = meanfield.guess(h,"random")
    scf = meanfield.hubbardscf(h,nk=20,mix=0.9,U=-U,mf=mf,filling=0.1)
    hscf = scf.hamiltonian
  #  rho = hscf.get_filling()
    d = -np.mean(hscf.extract("swave").real)
    f.write(str(U)+"  ")
    f.write(str(d)+"\n")
    f.flush()
f.close()
