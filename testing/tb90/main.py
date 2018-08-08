import geometry
import input_tb90

g = geometry.honeycomb_zigzag_ribbon(100)
#g = g.supercell(3)
h = g.get_hamiltonian()

h.write(output_file="hamiltonian_0.in")

in90 = input_tb90.tb90in()

#in90.write()

