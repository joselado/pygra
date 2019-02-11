from pygra import geometry
from pygra import sculpt
from pygra import specialgeometry
from pygra import specialhopping 


g = geometry.honeycomb_lattice()
g = g.supercell(4)
g1 = sculpt.remove_central(g,n=6) # second geometry


# get a twisted bilayer
g = specialgeometry.generalized_twisted_multilayer(5,gf=[g,g1],rot=[0,1])


h = g.get_hamiltonian(is_sparse=True,has_spin=False,is_multicell=False,
     mgenerator=specialhopping.twisted_matrix(ti=0.2,lambi=3.0))



h.get_bands(num_bands=40)
