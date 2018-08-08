# this script reads BANDS.OUT and yields the gap,
# considering only eigenvalues with a certain expectation value

import numpy as np

def gap():
  """ Get the gap weighted by eigenvalues"""
  m = np.genfromtxt("BANDS.OUT").transpose()
  e = m[1]
  v = np.abs(m[2])
  vcut = max(m[2])/10  # cutoff
  valence = min(e)
  conduction = max(e)
  for (ie,iv) in zip(e,v):
    if iv>vcut:
      if 0.>ie>valence:
        valence = ie 
      if 0.<ie<conduction:
        conduction = ie 
  g = conduction - valence
  return g

#if __name__=="main":
print gap()

