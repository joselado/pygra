module julia_hamiltonian
# dimension
using hamiltonians
function get_hamiltonian()
  h =hamiltonians.hamiltonian1d()
  intra = im*zeros(3,3)
  inter = 0.*intra

  # elements of the hamiltonian
  intra[1,2] = 1.0 + im*0.0
  intra[2,1] = 1.0 + im*0.0
  intra[2,3] = 1.0 + im*0.0
  intra[3,2] = 1.0 + im*0.0
  ###############

  inter[3,1] = 1.0 + im*0.0
  ###############

  h.intra = intra
  h.inter = inter
  return h
end
end
