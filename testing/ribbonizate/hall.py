import ribbonizate
import hamiltonians
import numpy as np


def bulk2ribbon(h,mag_field=0.05,n=10,sparse=True,check=True):
  """ Generate the Hamiltonian of a ribbon with magnetic field"""
  if not h.is_multicell: # dense hamiltonian
    ho = ribbonizate.hamiltonian_bulk2ribbon(h,n=n,sparse=sparse,check=check) # create hamiltonian
  else: # sparse hamiltonian
    import multicell
    ho = multicell.bulk2ribbon(h,n=n,sparse=sparse,nxt=6) # create hamiltonian
  ho.geometry.center()
  if np.abs(mag_field)>0.0000001: ho.add_peierls(mag_field) # add peierls phase
  return ho


def landau_levels(h,mag_field=0.01,k=0.0,nl=10,rfactor=1.5):
  """Return the energies of the Landau levels for a certain magnetic
  field"""
  nc = int(round(rfactor*h.geometry.a2[1]/mag_field)) # number of replicas
  hr = bulk2ribbon(h,mag_field=mag_field,n=nc,sparse=True) # generate ribbon
  import operators
  yop = operators.bulk1d(h,p=0.7) # bulk operator
  hamiltonians.lowest_bands(hr,kpath=[k],nbands=nl,info=True,operator=yop)
 



