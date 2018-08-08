import geometry  # library to create crystal geometries
import hamiltonians  # library to work with hamiltonians
import input_tb90 as in90
import heterostructures
import sys
import sculpt  # to modify the geometry
import numpy as np
import klist
import pylab as py
import green
import interactions
import islands


g = geometry.honeycomb_lattice()  # create a honeycomb lattice
g = islands.get_geometry(name="honeycomb",n=3,nedges=3,clean=True)
#g = geometry.honeycomb_lattice()  # create a honeycomb lattice
#g = geometry.square_ribbon(1) 
#g = g.supercell(2)  # double supercell
#g = geometry.honeycomb_zigzag_ribbon(10) 
h = hamiltonians.hamiltonian(g) # create hamiltonian
h.first_neighbors()  # create first neighbor hopping
h.add_rashba(.2)
#h.set_finite_system()
h.write(output_file="hamiltonian_0.in")
h.write(output_file="hamiltonian.in")
#h.set_finite_system()
old_mf = interactions.antiferro_initialization(h)
#old_mf = interactions.ferro_initialization(h)
ab = interactions.hubbard(h,2.0) # mean field operators
import random
rand = random.random

##############################
# create a custom mean field #
##############################
v = np.array([rand(),rand(),rand()])
#v = np.array([0.,0.,1.])
vecs = [v*(-1)**i for i in range(len(h.intra)/2)] # create AF initialization
vecs = [v for i in range(len(h.intra)/2)] # create AF initialization
mf = interactions.directional_mean_field(vecs) # create mean field matrix 
in90.write_mean_field(mf) # write in file

##############################
##############################
##############################
#vecs = [[rand(),0.,rand()] for x in h.geometry.x]
#vecs = [[0.,0.,0.] for x in h.geometry.x]
#ab = interactions.directional_hubbard(vecs,g=2.0) # mean field operators
#interactions.write_ab_mf(ab)
#exit()
#mf = interactions.selfconsistency(h,old_mf=old_mf,nkp=20,ab_list=ab)
scf = interactions.hubbardscf(h,U=1.0,nkp=10,mag=vecs,silent=False) 


import rotate_spin as rs
R = rs.rotation_matrix(h.intra,scf.magnetization)

#h.intra = R*h.intra*R.H # rotate intracell matrix
#scf.mean_field = R*scf.mean_field*R.H # rotate mean field

print("NEW")
scf = interactions.hubbardscf(h,U=1.0,nkp=10,mf=scf.mean_field,
                   silent=False,collinear=False) 
h.geometry.write()

h = scf.hamiltonian # get the Hamiltonian

#exit()

h.get_bands()


py.show()
