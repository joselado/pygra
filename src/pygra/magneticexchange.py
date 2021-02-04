# routines to compute magnetic exchange
import numpy as np


def NN_exchange(h,J=0.1,nk=2,num_bands=None):
    """Compute the nearest neighbor exchange using
    a brute force algorithm"""
    from pygra import ldos
    d = ldos.ldos_density(h,nk=nk,delta=1e-3,num_bands=num_bands) # get the density
    hs = h.supercell([2,1,1]) # get a supercell
    ds0 = J*np.concatenate([d,d]) # FE configuration
    ds1 = J*np.concatenate([d,-d]) # AF configuration
    if h.has_spin: # spinful version
        ds0 = np.array([0*ds0,0*ds0,ds0]).T # magnetizations
        ds1 = np.array([0*ds1,0*ds1,ds1]).T # magnetizations
        hs0 = hs.copy()
        hs1 = hs.copy()
        hs0.add_zeeman(ds0) # add the Zeeman field
        hs1.add_zeeman(ds1) # add the Zeeman field
        e0 = hs0.get_total_energy(nk=nk,nbands=num_bands) # ground state energy 
        e1 = hs1.get_total_energy(nk=nk,nbands=num_bands) # ground state energy 
        return e1-e0
    else: # spinless version
        hs0u = hs.copy()
        hs0d = hs.copy()
        hs1u = hs.copy()
        hs1d = hs.copy()
        hs0u.add_onsite(ds0)
        hs0d.add_onsite(-ds0)
        hs1u.add_onsite(ds1)
        hs1d.add_onsite(-ds1)
        gete = lambda h0: h0.get_total_energy(nk=nk,nbands=num_bands) 
        return gete(hs1u) + gete(hs1d) - gete(hs0u) - gete(hs0d)



