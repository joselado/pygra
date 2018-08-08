
# library for setting up several systems
import geometry
import hamiltonians

def graphene_armchair_ribbon(ntetramers=1,lambda_soc=0.0):
  """ Creates teh hamiltonian for a graphene armchair ribbon"""
  g = geometry.honeycomb_armchair_ribbon(ntetramers) # create the geometry
  h = hamiltonians.hamiltonian(g) # create the hamiltonian
  # get the intracell and intercell terms
  (intra,inter) = hamiltonians.kane_mele(g.x,g.y,
                    celldis=g.celldis,lambda_soc=lambda_soc)
  h.intra = intra # assign intracell
  h.inter = inter # assign intercell
  return h # return hamiltonian



def graphene_zigzag_ribbon(ntetramers=1,lambda_soc=0.0):
  """ Creates teh hamiltonian for a graphene armchair ribbon"""
  g = geometry.honeycomb_zigzag_ribbon(ntetramers) # create the geometry
  h = hamiltonians.hamiltonian(g) # create the hamiltonian
  # get the intracell and intercell terms
  (intra,inter) = hamiltonians.kane_mele(g.x,g.y,
                    celldis=g.celldis,lambda_soc=lambda_soc)
  h.intra = intra # assign intracell
  h.inter = inter # assign intercell
  return h # return hamiltonian



def kane_mele_ribbon(g,lambda_soc=0.0,mag_field=0.0):
  """ Creates teh hamiltonian for a kane_mele ribbon, input is geometry"""
  h = hamiltonians.hamiltonian(g) # create the hamiltonian
  # get the intracell and intercell terms
  (intra,inter) = hamiltonians.kane_mele(g.x,g.y,
                    celldis=g.celldis,lambda_soc=lambda_soc,
                    mag_field = mag_field)
  h.intra = intra # assign intracell
  h.inter = inter # assign intercell
  h.num_orbitals = len(g.x) # assign number of orbitals
  return h # return hamiltonian






