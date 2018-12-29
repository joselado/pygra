# Add the root path of the pygra library
import os ; import sys ; sys.path.append(os.environ['PYGRAROOT'])

import numpy as np
from pygra import neighbor
from pygra import multiterminal
from pygra import geometry
from pygra import sculpt
from pygra import skeleton
g = geometry.honeycomb_lattice()
gs = geometry.square_lattice()
#h = g.get_hamiltonian(has_spin=False)
#h = skeleton.image2island("island.png",h,s=10)
#h.geometry.write()
imfile = "color_island.png"
imfile = "pristine_v2.png"
#imfile = "left_up.png"
gl = sculpt.image2island(imfile,gs,size=20,color="red")
gc = sculpt.image2island(imfile,g,size=20,color="black")
gr = sculpt.image2island(imfile,gs,size=20,color="blue")
# vectors connecting the 
Rdr = np.array([max(gr.x) - min(gr.x) + 1.0,0.,0.])
Ldr = np.array([max(gl.x) - min(gl.x) + 1.0,0.,0.])
gr.a1 = Rdr # vector
gl.a1 = -Ldr # vector
gr.dimensionality = 1
gl.dimensionality = 1
#gc.write()
#exit()
# create the device
dev = multiterminal.Device() # create the devide object
dev.biterminal(right_g=gr,left_g=gl,central_g=gc,disorder=0.4)
dev.write()
dev.write_current(energy=0.5)
#exit()
#print(dev.transmission(energy=0.5))
# turn oen dimensional
