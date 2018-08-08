import geometry
import multicell
import hall

g = geometry.honeycomb_lattice()
# g = geometry.square_lattice()
h = g.get_hamiltonian()
h.remove_spin()

h = multicell.turn_multicell(h)
#h = multicell.rotate(h)

hr = hall.bulk2ribbon(h,mag_field=0.01,n=80,sparse=True)

# hr = multicell.bulk2ribbon(h,n=40,sparse=False)

#hr.geometry.write()




hr.get_bands()

