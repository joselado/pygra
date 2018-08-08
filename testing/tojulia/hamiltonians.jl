module hamiltonians
export hamiltonian1d, hamiltonian2d

type hamiltonian1d
  """Hamiltonian type"""
  intra # intraterm
  inter # interterm
  function hamiltonian1d()
    intra = [0. 1. ; 1. 0.] # intra matrix
    inter = 0.*intra # intra matrix
    new(intra,inter) # intialize the object
    end
  end

type hamiltonian2d
  """Hamiltonian type"""
  intra # intraterm
  tx
  ty
  txy
  txmy
  function hamiltonian1d()
    m = [0. 0. ; 0. 0.] # intra matrix
    new(m,m,m,m,m) # intialize the object
    end
  end

end
