# library to calculate dielectric responses with Hubbard

using hamiltonians

function get_hk(h::hamiltonian1d,k::Float64)
  """Calculates k dependent hamiltonian""" 
  tk = h.inter*exp(im*pi*k*2.)  # complex hopping
  hk = Hermitian(h.intra + tk + conj(transpose(tk))) # create H(k)
  return hk
  end

function eigk(h::hamiltonian1d,k::Float64)
  """Calculates k dependent eigenvalues""" 
  return eig(get_hk(h,k)) # get eigenvalues
  end

function occ(ene)
  """Calculates occupation"""
  if ene<0. return 1.
  end
  return 0.
end

function lindhard_tensor(a,b)
  """Defines the tensorial product"""
  ab = im*zeros(length(a),length(b)) # create matrix
  for i in 1:length(a) # loop over rows 
    for j in 1:length(b) # loop over columns
      ab[i,j] = conj(a[i])*b[i]*a[j]*conj(b[j])
    end
  end
  return ab
end

function calculate_chi0(h::hamiltonian1d ; q=0.01,energies=[0.])
  """Calcultes the dielectric response at a certain energy"""
  nk = 2000
  ks = [float(i)/nk for i in 1:nk] # create kpoints
  c = h.intra*0. # array for the chi response
  chis = [c for i in energies] # create array with responses
  jeps = im*0.002 # analitic continuation
  for k in ks # loop over ks
    enesi,evecsi = eigk(h,k)  # diagonalize
    enesj,evecsj = eigk(h,k+q)  # diagonalize
  #  enesj,evecsj = eigk(h,k+q)  # diagonalize
    for i in 1:length(enesi) # loop over eigenvectors
      vi = evecsi[:,i] # get eigenvector
      ei = enesi[i] # get eigenvalue
      for j in 1:length(enesj) # loop over eigenvectors
        vj = evecsj[:,j] # get eigenvector
        ej = enesj[j] # get eigenvalue
        vij = lindhard_tensor(vi,vj) # create the tensor
        mij = (occ(ei)-occ(ej))*vij # multiply by the occupation
     #   rs = @parallel for ie in 1:length(energies) # launch energies
     #            mij/(ei-ej-energies[ie]+jeps) 
     #   end
     #   for ie in 1:length(energies) # collect energies
     #     chis[ie] += fetch(rs[i])
     #   end 
        for ie in 1:length(energies) # loop over energies
          chis[ie] += mij/(ei-ej-energies[ie]+jeps) 
     #     chis[ie] += fetch(r)
        end
      end
    end
  end
  return chis/nk
  end
 

function calculate_chi_RPA(chis ; energies=[0.], U = 1.0)
  """ Calculates Chi by using the RPA appoximation"""
  crpa = chis *0.0 # create an array of chis
  print(chis[1])
  I = eye(int(sqrt(length(chis[1])))) # identity matrix
  for i in 1:length(chis)
    crpa[i] = (1./(I - U*chis[i]))*chis[i]
  end
  return crpa
end



function calculate_chi(h::hamiltonian1d ; q=0.01,energies=[0.],U=1.0)
  """Calculates Chi by RPA, return an array of matrices"""
  chis = calculate_chi0(h ; energies = energies, q=q) # calculate by lin res
  chis = calculate_chi_RPA(chis , energies=energies, U = U) # perform RPA
  return chis # return matrices
end


function charge_stiffness(h::hamiltonian1d, energies ; U=1.0, q=0.01)
  """Calculate the charge stiffness"""
  chis = calculate_chi0(h ; energies = enes, q=q) # calculate linear response
  chis = calculate_chi_RPA(chis , energies=enes, U = U) # calculate RPA
  e2 = [ie*ie for ie in energies] # calculate omega**2
  q2 = q*q # calculate q**2
  Ks = chis # rename the response
  Ks = [chis[i]*e2[i]/q2 for i in 1:length(energies)] # calculate K
  Ks = [sum(k) for k in Ks]  # sum all the contributions
  return Ks
end





function write_xy(x,y,name)
  """Writes xy array in a file"""
  f = open(name,"w")  # open file
  for i in 1:length(x)  # loop over elements
    write(f,string(x[i]),"   ",string(y[i]),"\n")
  end
  close(f) # close file
end

import julia_hamiltonian

h = julia_hamiltonian.get_hamiltonian()
enes = linspace(-.1,.1,500) # list of energies
q = 0.0001 # q vector
q = q*int(sqrt(length(h.intra)))
U = 1.0
#chis = calculate_chi(h ; energies = enes, q=q,U=U)
chis = calculate_chi0(h ; energies = enes, q=q)
#chis = charge_stiffness(h,enes,U=1.0,q=0.001)
chis = [sum(chi) for chi in chis]
chir = [real(c) for c in chis]
chii = [imag(c) for c in chis]
write_xy(enes,chir,"CHI_R.OUT")
write_xy(enes,chii,"CHI_I.OUT")



