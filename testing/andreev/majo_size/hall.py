import ribbonizate
import numpy as np


def bulk2ribbon(h,mag_field=0.05,n=10,sparse=True,check=True):
  """ Generate the Hamiltonian of a ribbon with magnetic field"""
  if not h.is_multicell: # dense hamiltonian
    ho = ribbonizate.hamiltonian_bulk2ribbon(h,n=n,sparse=sparse,check=check) # create hamiltonian
  else: # sparse hamiltonian
    from skeleton import build_ribbon
    import geometry
    gsk = geometry.square_ribbon(n) # skeleton geometry
    ho = build_ribbon(h,g=gsk,n=n) # build the geometry
  ho.geometry.center()
  if np.abs(mag_field)>0.0000001: ho.add_peierls(mag_field) # add peierls phase
  return ho
