import multicell

def build(h,nz=1):
  """Create Hamiltonian of a film from a 3d geometry"""
#  if not h.dimensionality==3: raise
  ho = multicell.supercell(h,nsuper=[1,1,nz],sparse=False,ncut=3)
  ho.dimensionality = 2 # reduce dimensionality
  hoppings = [] # empty list
  for t in ho.hopping: # loop over hoppings
    if t.dir[2]== 0: hoppings.append(t) # remove in the z direction
  ho.hopping = hoppings # overwrite hoppings
  return ho
