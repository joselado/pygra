# Add the root path of the pygra library
import os ; import sys ; sys.path.append(os.environ['PYGRAROOT'])
import numpy as np

### WARNING, this script only works in a special cluster! (Triton) ###

def func_to_parallelize(U):
    """Function to parallelize"""
    # all the variables must be internal!
    from pygra import geometry
    from pygra import meanfield
    g = geometry.honeycomb_lattice()
    g.write()
    Us = np.linspace(0.,4.,10) # different Us
    h = g.get_hamiltonian() # create hamiltonian of the system
    mf = meanfield.guess(h,mode="antiferro") # antiferro initialization
    # perform SCF with specialized routine for Hubbard
    scf = meanfield.hubbardscf(h,nk=20,filling=0.5,U=U,verbose=1,
                  mix=0.9,mf=mf)
    # alternatively use
    h = scf.hamiltonian # get the Hamiltonian
    gap = h.get_gap() # compute the gap
    return gap

from pygra import parallelslurm

Us = np.linspace(0.,3.0,10) # 10 different calculations
gs = parallelslurm.pcall(func_to_parallelize,Us) # compute for all the inputs
print(gs)
np.savetxt("SWEEP.OUT",np.array([Us,gs]).T)
