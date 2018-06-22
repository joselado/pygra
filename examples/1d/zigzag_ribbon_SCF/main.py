# zigzag ribbon
import sys
sys.path.append("../../../pygra")  # add pygra library

import geometry
import scftypes
import operators
g = geometry.honeycomb_zigzag_ribbon(4) # create geometry of a zigzag ribbon
h = g.get_hamiltonian() # create hamiltonian of the system

mf = scftypes.guess(h,"ferro",fun=lambda r: [0.,0.,1.])
scf = scftypes.selfconsistency(h,nkp=30,filling=0.5,mf=mf,
             mode="Hubbard collinear")
h = scf.hamiltonian # get the Hamiltonian
#op = operators.get_sz(h)
#print(op.shape)
#h.add_zeeman([0.,0.,4])
h.get_bands(operator=operators.get_sz(h)) # calculate band structure
#print(scf.magnetization)
h.write()
