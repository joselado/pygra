import geometry  # library to create crystal geometries
import systems  # library which yields several systems
import hamiltonians  # library to work with hamiltonians
import heterostructures  # library for heterostructures
import numpy as np
import pylab as py
import input_tb90 as in90
import scipy.sparse.linalg as lg
from green import read_sparse
from time import clock
import os

# file
file_eigen = "eigen_heff.dat"
os.remove(file_eigen)
with open(file_eigen, "a") as myfile:
  myfile.write("# Swave  Real Imag")



neig = 2 # number of eigenvalues
fig_mu = py.figure()
fig_mu.set_facecolor("white")
sfig_mu = fig_mu.add_subplot(111)

svalues = np.arange(0.0,0.5,0.02)
for sval in svalues:  
#  g = geometry.honeycomb_armchair_ribbon(ntetramers=15)
  g = geometry.honeycomb_armchair_ribbon(ntetramers=25)
  
  # create hamiltonians heterojunction
  h_right = hamiltonians.hamiltonian(g)
  h_left = hamiltonians.hamiltonian(g)
  
  # central is QSH
  h_right.get_simple_tb()
  h_left.get_simple_tb()
  
  
  h_left.read(input_file="hamiltonian_canted_25.in")
  
  # shift fermi energy
  mu = 0.04
  h_right.shift_fermi(0.4)
  h_left.shift_fermi(mu)

  
  # electron hole sector
#  h_right.add_swave_electron_hole_pairing(delta=sval,phi=0.0)
  h_right.add_swave_electron_hole_pairing(delta=sval,phi=0.0)
  h_left.add_swave_electron_hole_pairing(delta=0.,phi=0.0)

  # hybrid right part
  h_right = hamiltonians.create_hybrid(h_right,h_left)  
  
  
  from time import clock
  told = clock()
  h_list = [h_left for i in range(5)]
  h_list += [h_right for i in range(5)]
  # create heterojunctions
  hj_uniform = heterostructures.create_leads_and_central_list(h_right,h_left
                  ,h_list)
  
  
  
  
  eig = heterostructures.eigenvalues(hj_uniform,numeig=5,effective=True)
  eig = sorted(zip(eig.real,eig.imag)) # sort eigenvalues 
  
  
  for e in eig:  # plot
    sfig_mu.scatter(sval,e[0])  
    print sval,e[0],e[1]
  # write in the file
  with open(file_eigen, "a") as myfile:
    myfile.write("\n"+str(sval)+"  ")
    for e in eig:  # plot
      myfile.write(str(e[0])+"  "+str(e[1])+"  ")



py.show()

