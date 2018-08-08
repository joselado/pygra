import geometry  # library to create crystal geometries
import hamiltonians  # library to work with hamiltonians
import input_tb90 as in90
import heterostructures
import multilayers
import os
import numpy as np


g = geometry.honeycomb_zigzag_ribbon(ntetramers=1)
g = geometry.square_ribbon(1)
#g.supercell(2)
h = hamiltonians.hamiltonian(g) 

h.get_simple_tb()
#h.get_simple_tb(mag_field=0.1)
#h.add_zeeman([0.0,0.02,0.])
#h.add_kane_mele(0.1)



if False:
  h.write(output_file = "hamiltonian_0.in")
  os.system("cp tb90.in-scf tb90.in")
  os.system("tb90.x")
#in90.tb90in().write()

if False:
  h.read("hamiltonian.in")
  mag = in90.read_magnetization()  # ground state magnetism
  h.align_magnetism(mag)
  h.write()
  os.system("cp tb90.in-bands tb90.in")
  os.system("tb90.x")

if False:
#  h.read("hamiltonian.in")
  h.global_spin_rotation(vector = [1.,0.,0.],angle=0.5)
  h.write(output_file = "hamiltonian_0.in")


if False:
  h.generate_spin_spiral(vector = [1.,0.,0.],angle=1.)
  h.write(output_file = "hamiltonian_0.in")





if False: 
  tb90in = in90.tb90in()
  tb90in.mode("total_energy")
  tb90in.set_hubbard(2.0)
  tb90in.write()
  tb90in.run()

if True:
#  h.read("hamiltonian-ac.in")
  h.read("hamiltonian-zz.in")
  atoms = [0,len(h.intra)/2] # atoms to rotate
  atoms = None # atoms to rotate
  qrange = np.linspace(0.,.16,100)
  vector = np.array([0.,0.,1.])
  # spin stiffness calculation
  in90.script_spin_stiffness(h,qrange=qrange,vector=vector,atoms=atoms) 



