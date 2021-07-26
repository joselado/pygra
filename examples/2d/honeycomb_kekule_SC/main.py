# Add the root path of the pygra library
import os ; import sys 
sys.path.append(os.path.dirname(os.path.realpath(__file__))+"/../../../src")





import numpy as np
from pygra import geometry
from pygra import films
from pygra import meanfield


g = geometry.honeycomb_lattice()
g = g.supercell(3)
h = g.get_hamiltonian()
h.turn_nambu()
mf = meanfield.guess(h,"random")
scf = meanfield.Vinteraction(h,V1=-2.0,V2=-1.0,mf=mf,
        nk=20,filling=0.5,mix=0.6,
        compute_normal=True,
        compute_dd=False,
        compute_anomalous=True)
h = scf.hamiltonian
h.write_anomalous_hopping()
print(scf.identify_symmetry_breaking())
h.get_bands(operator="sz")









