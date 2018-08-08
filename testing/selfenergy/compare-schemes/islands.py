import geometry
import sculpt
import numpy as np


def get_geometry(name="square",n=5,nedges=None,rot=0.,clean=True):
  """ Create a 0d island"""
  lattice_name = name
  if lattice_name=="honeycomb":
    geometry_builder = geometry.honeycomb_lattice
    if nedges==None: nedges = 6
  elif lattice_name=="square":
    geometry_builder = geometry.square_lattice
    if nedges==None: nedges = 4
  elif lattice_name=="kagome":
    geometry_builder = geometry.kagome_lattice
    if nedges==None: nedges = 3
  elif lattice_name=="lieb":
    geometry_builder = geometry.lieb_lattice
    if nedges==None: nedges = 4
  elif lattice_name=="triangular":
    geometry_builder = geometry.triangular_lattice
    if nedges==None: nedges = 3
  else: raise
  # first create a raw unit cell
  g = geometry_builder()  # build a 2d unit cell
  nf = float(n)   # get the desired size, in float
  g = g.supercell(7*n)   # create supercell
  g.set_finite() # set as finite system
  g.center() # center the geometry
  # now scuplt the geometry
  g = sculpt.rotate(g,rot) # initial rotation
  def f(x,y): return x>-nf*(np.cos(np.pi/3)+1.)  # function to use as cut
  for i in range(nedges): # loop over rotations, 60 degrees
    g = sculpt.intersec(g,f) # retain certain atoms
    g = sculpt.rotate(g,2.*np.pi/nedges) # rotate 60 degrees
  if clean: # if it is cleaned
    g = sculpt.remove_unibonded(g)  # remove single bonded atoms
  g.center() # center the geometry
  return g



