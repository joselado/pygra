# Add the root path of the pygra library
import os ; import sys ; sys.path.append(os.environ['PYGRAROOT'])

from pygra import geometry
g = geometry.triangular_lattice_tripartite()
g.write()
