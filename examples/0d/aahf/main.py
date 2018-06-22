
import sys
sys.path.append("../../../pygra")  # add pygra library
import geometry
import numpy as np

g = geometry.chain(400) # chain
g.dimensionality = 0

betas = np.linspace(0.0,4.0,30)
# loop over v's

def discard(w):
  w2 = np.abs(w)*np.abs(w) # absolute value
  n = len(w)
  if np.sum(w2[0:n//10])>0.5 or np.sum(w2[9*n//10:n])>0.5: return False
  else: return True

fo = open("LAMBDA_VS_V.OUT","w")
for beta in betas:
  h = g.get_hamiltonian(has_spin=False)
  import potentials
  fun = potentials.aahf1d(v=2.5,beta=beta)
  h.shift_fermi(fun)
  (es,ls) = h.get_tails(discard=discard) # return the localization length
  for (e,l) in zip(es,ls):
    fo.write(str(beta)+"    ")
    fo.write(str(e)+"    ")
    fo.write(str(l)+"\n")
  fo.flush()

fo.close()

h.get_bands()
