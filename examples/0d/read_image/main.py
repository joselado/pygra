# Add the root path of the pygra library
import os ; import sys ; sys.path.append(os.environ['PYGRAROOT'])

import numpy as np
from pygra import neighbor
from pygra import multiterminal
from pygra import geometry
from pygra import sculpt
from pygra import skeleton
g = geometry.honeycomb_lattice()
imfile = "island.png"
g = sculpt.image2island(imfile,g,size=20,color="black")
g.write()
