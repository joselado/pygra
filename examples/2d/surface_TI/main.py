# zigzag ribbon
import sys
sys.path.append("../../../pygra")  # add pygra library

from surface_TI import hamiltonian # this function will yield the Hamiltonian

h = hamiltonian(mw=1.0) # get the Hamiltonian, mw is the Wilson mass

h.get_bands() # get the bandstructure

