import geometry  # library to create crystal geometries
import hamiltonians  # library to work with hamiltonians
import input_tb90 as in90
import heterostructures
import multilayers
import os
import numpy as np
import green
import pylab as py

g = geometry.honeycomb_zigzag_ribbon(ntetramers=2)
#g = geometry.square_ribbon(1)
#g.supercell(4)
h = hamiltonians.hamiltonian(g) 
h.get_simple_tb() # get hamiltonian


#h.add_antiferromagnetism(.2)
#h.add_rashba(.4)
#h.shift_fermi(-1.4)
#h.add_zeeman([.2,0.,0.])
#h.add_swave(delta = .05)

h.plot_bands()

py.figure()

from time import clock

es = np.linspace(-3.0,3.0,500)
told = clock()
if True:
  bulk = []
  surf = []
  for e in es:
    dos_bulk,dos_surf = green.green_renormalization(h.intra,
                        h.inter,energy=e)
    bulk.append(-dos_bulk.trace()[0,0].imag)
    surf.append(-dos_surf.trace()[0,0].imag)
  py.plot(es,surf,color="blue",marker="o")
  py.plot(es,bulk,color="red",marker="x")

print told-clock()
told = clock()

if False:
  for e in es:
    dos = green.dyson(h.intra,h.inter,energy = e)
    dos = -dos.trace()[0,0].imag
    py.scatter(e,dos,color="red",marker="x")
print told-clock()




py.show()
