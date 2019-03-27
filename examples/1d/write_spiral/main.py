from pygra import geometry
from pygra import scftypes
import numpy as np
# create the hamiltonian
g = geometry.triangular_lattice() # triangular lattice geometry
g = geometry.chain()
g.supercell(2)
h = g.get_hamiltonian(has_spin=True) # create hamiltonian of the system
###################

# This is the direction around which we rotate the magnetization
vector = [1.,0.,0.]
q = np.array([0.1,0.0,0.0])
# rotate the Hamiltonian
h.add_zeeman([0.,4.,0.0])
h.generate_spin_spiral(vector=vector,qspiral=-q,fractional=True)
#h = h.supercell(4)
h.write_magnetization()

