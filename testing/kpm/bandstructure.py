
# special band structures

import topology
import operators

def berry_bands(h,klist=None,mode=None,operator=None):
  """Calculate band structure resolved with Berry curvature"""
  ks = [] # list of kpoints
  if mode is not None: # get the mode
    if mode=="sz": operator = operators.get_sz(h)
    else: raise

  fo = open("BANDS.OUT","w")
  for ik in range(len(klist)): # loop over kpoints
    (es,bs) = topology.operator_berry_bands(h,k=klist[ik],operator=operator)
    for (e,b) in zip(es,bs):
      fo.write(str(ik)+"    "+str(e)+"    "+str(b)+"\n")
  fo.close()
