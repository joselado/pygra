# specialized routine to perform an SCF, taking as starting point an
# attractive local interaction in a spinless Hamiltonian

from ..sctk.spinless import onsite_delta_vev

def scfswave(h,nk=8,**kwargs):
    """Perform the SCF mean field"""
    if not h.check_mode("spinless"): raise # sanity check
    h0 = h.copy() # initial Hamiltonian
    d = onsite_delta_vev(h,nk=nk) # compute the pairing
    h.add_pairing(d) # add the pairing to the Hamiltonian
    ## not finished ##

