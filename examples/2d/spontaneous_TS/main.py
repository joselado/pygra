# Add the root path of the pygra library
import os ; import sys ; sys.path.append(os.environ['PYGRAROOT'])

import numpy as np
from pygra import geometry
from pygra import films
from pygra import meanfield


g = geometry.diamond_lattice()
g = films.geometry_film(g,nz=2)
g = g.supercell(3)
g.write()
h = g.get_hamiltonian(has_spin=False)
#h.add_kekule(.1)
#h.add_sublattice_imbalance(lambda r: 0.6*np.sign(r[2]))
h.add_antiferromagnetism(lambda r: 0.6*np.sign(r[2]))
#h.add_swave(lambda r: 0.6*(r[2]<0))
#h.add_swave(0.0)
mf = meanfield.guess(h,"kanemele")
mf = meanfield.guess(h,"random")
#mf = None
scf = meanfield.Vinteraction(h,V1=0.4,U=0.0,mf=mf,
        V2=0.3,nk=6,filling=0.5,mix=0.3)
h = scf.hamiltonian
#h.add_rashba(.1)
#h.add_kane_mele(0.1)
#h.add_antiferromagnetism(lambda r: 0.6*(r[2]>0))
#h.add_swave(lambda r: 0.6*(r[2]<0))
#print(h.extract("swave"))
#print(h.extract("density"))
#print(h.extract("mx"))
#print(h.extract("my"))
#print(h.extract("mz"))
#h.add_zeeman([.0,.0,.1])
#h.write_onsite()
#op = h.get_operator("sz")#*h.get_operator("sublattice")
op = h.get_operator("valley")#*h.get_operator("sublattice")
h.get_bands(operator=op)
