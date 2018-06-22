
import sys
sys.path.append("../../../pygra")  # add pygra library
import islands
import interactions
import numpy as np

g = islands.get_geometry(name="honeycomb",n=4,nedges=3,rot=0.0) # get an island

# maximum distance to the origin
rmax = np.sqrt(np.max([ri.dot(ri) for ri in g.r]))

def fhop(r1,r2):
  """Function to calculate the hopping, it will create different hoppings
  for different atoms. The hopping becomes smaller the further the atom
  is from the origin"""
  tmax = 1.0 # minimum hopping
  tmin = 0.7 # maximum hopping
  dr = r1-r2 # vector between the two sites
  drmod = np.sqrt(dr.dot(dr)) # distance
  rm = (r1+r2)/2. # average position
  rmmod = np.sqrt(rm.dot(rm)) # value of the average position
  if 0.9<drmod<1.1: # if first neighbor
    lamb = rmmod/rmax # ratio between 0 and 1
    return tmax*(1.-lamb) + tmin*lamb
  else: return 0.0



h = g.get_hamiltonian(fun=fhop,has_spin=True) # get the Hamiltonian

g.write()
import scftypes
scf = scftypes.hubbardscf(h,U=1.0,mag=[[1,0,0] for r in g.r])
scf.hamiltonian.get_bands()
