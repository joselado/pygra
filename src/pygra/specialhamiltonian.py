from . import specialhopping
from . import specialgeometry
import numpy as np
from . import geometry


def tbg(n=7,ti=0.12,lambi=3.0,lamb=3.0,is_sparse=True,
        has_spin=False,dl=3.0):
    """
    Return the Hamiltonian of twisted bilayer graphene
    """
    g = specialgeometry.twisted_bilayer(n,dz=dl/2.0)
    mgenerator = specialhopping.twisted_matrix(ti=ti,
            lambi=lambi,lamb=lamb,dl=dl)
    h = g.get_hamiltonian(is_sparse=is_sparse,has_spin=has_spin,
            is_multicell=True,mgenerator=mgenerator)
    return h


def multilayer_graphene(l=[0],real=False,**kwargs):
  """Return the hamiltonian of multilayer graphene"""
  g = specialgeometry.multilayer_graphene(l=l)
  g.center()
  if real: # real tight binding hopping
      mgenerator = specialhopping.twisted_matrix(**kwargs)
      h = g.get_hamiltonian(has_spin=False,
          mgenerator=mgenerator)
  else:
    h = g.get_hamiltonian(has_spin=False,
          fun=specialhopping.multilayer(**kwargs))
  return h


def flux2d(g,n=1,m=1):
    """Return a Hamiltonian with a certain commensurate flux per unit cell"""
    from pygra import sculpt
    from pygra import supercell
    g = supercell.target_angle(g,0.5) # target a orthogonal cell
    g = sculpt.rotate_a2b(g,g.a1,np.array([1.,0.,0.])) # set in the x direction
    g = g.supercell([1,n,1])
    h = g.get_hamiltonian(has_spin=False)
    r = np.array([0.,1.,0.])
    dr = g.a2.dot(r) # distance
    h.add_peierls(m*2.*np.pi/dr)
    return h



def valence_TMDC(g=None,soc=0.0,**kwargs):
    """Return the Hamiltonian for the valence band of a TMDC"""
    if g is None:
        g = geometry.triangular_lattice()
    ft = specialhopping.phase_C3_matrix(g,phi=soc,**kwargs)
    h = g.get_hamiltonian(mgenerator=ft,is_multicell=True,has_spin=False)
    h.turn_spinful(enforce_tr=True)
    return h # return the Hamiltonian



def NbSe2(soc=0.0,cdw=0.0,g=None):
    """Return the Hamiltonian of NbSe2"""
    if g is None: 
        g = geometry.triangular_lattice()  # triangular lattice
        if cdw!=0.0: g = g.supercell(3)
#    ts = np.array([86.8,139.9,29.6,3.5,3.3])
#    ts = np.array([46.,257.5,4.4,-15,6])
    ts = np.array([0.3,2.,0.6,0.2,0.])
    t = ts[0]/np.max(ts) # 1NN 
#    ts[0] = 0.0 # set to zero
    ts = ts/np.max(ts) # normalize
    fm = specialhopping.neighbor_hopping_matrix(g,ts) # function for hoppings
    h = g.get_hamiltonian(mgenerator=fm,is_multicell=True,has_spin=False,
            cutoff=len(ts))
    ## Now add the SOC if necessary
    if soc!=0.0: # add the SOC
        h.turn_spinful() # turn spinful
        d = g.neighbor_distances()[1]
        d = 1.0
        hsoc = valence_TMDC(g=h.geometry,soc=soc,d=d) # hamiltonian with SOC
        h = h + t*hsoc # add the two Hamiltonians
    if cdw!=0.0: # add the CDW
        g0 = geometry.triangular_lattice()  # triangular lattice
        g0 = g0.supercell(3) # create a supercell
        from . import potentials
        f0 = potentials.commensurate_potential(g0,n=6,angle=np.pi/6.,
                k=1./np.sqrt(3)*2.)
        f0 = f0.normalize()*cdw
        f0 = f0.set_average(0.)
        rc = np.mean(h.geometry.get_closest_position([.1,.1,0.],n=3),axis=0)
        f = lambda r: f0(r-rc)
        h.geometry.write_profile(f)
        h.add_onsite(f)
    h.set_filling(.5)
#    h = h.supercell(4)
#    m = np.array(h.intra.todense()).reshape(h.intra.shape[0]**2)
    return h
    



def triangular_pi_flux(g=None,**kwargs):
    """Return a pi-flux Hamiltonian"""
    raise # this does not work yet
    if g is None: # no geometry given
        g = geometry.triangular_lattice() # geometry of a traingular lattice
    g = g.supercell((1,2)) # create a supercell with 2 atoms
    h = g.get_hamiltonian(**kwargs) # return the Hamiltonian
    h.add_peierls(1*np.pi*2./np.sqrt(3.)) # add the magnetic field
    if h.has_time_reversal_symmetry(): pass
    else: 
        print("Something wrong happened in pi-flux")
        raise
    return h








