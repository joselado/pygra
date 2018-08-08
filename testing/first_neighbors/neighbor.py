import numpy as np

def find_first_neighbor(r1,r2):
   """Calls the fortran routine"""
   import first_neighborsf90 as fn
   nn = fn.number_neighborsf90(r1.T,r2.T)
   pairs = np.array(fn.first_neighborsf90(r1.T,r2.T,nn)).T
   return pairs # return the pairs


