# specialized routine to perform an SCF, taking as starting point an
# attractive local interaction in a spinless Hamiltonian

from ..sctk.spinless import onsite_delta_vev

def scfswave(h0,u=0.0,nk=8,**kwargs):
    """Perform the SCF mean field"""
    if not h0.check_mode("spinless"): raise # sanity check
    h = h0.copy() # initial Hamiltonian
    dold = np.random.random(h.intra.shape[0]) # random guess
    do_scf = True
    while do_scf:
      h = h0.copy() # copy Hamiltonian
      h.add_pairing(d*u) # add the pairing to the Hamiltonian
      d = onsite_delta_vev(h,nk=nk) # compute the pairing
      diff = np.max(np.abs(d-dold)) # compute the difference
      print("Error = ",diff) # Difference
      if diff<1e-5: 
          do_scf = False
          scf.hamiltonian = h # store
    return scf # return SCF object



class SCF(): pass

