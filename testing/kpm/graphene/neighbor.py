from __future__ import print_function
import numpy as np




def find_first_neighbor(r1,r2):
   """Calls the fortran routine"""
   import first_neighborsf90 as fn
   r1t = r1.T
   r2t = r2.T
   nn = fn.number_neighborsf90(r1t,r2t)
#   print nn
   if nn==0: return []  # if no neighbors found
   pairs = np.array(fn.first_neighborsf90(r1t,r2t,nn))
   return pairs.T # return the pairs



try: 
  import first_neighborsf90
except:
  print("ERROR, fortran routine is not well compiled")
  def find_first_neighbor(r1,r2):
     """Calls the fortran routine"""
     print("Using ultraslow function!!!!!!!!!!")
     pairs = []
     for i in range(len(r1)):
       for j in range(len(r1)):
         ri = r1[i]
         rj = r2[j]
         dr = ri-rj
         dr = dr.dot(dr)
         if 0.8<dr<1.2: pairs.append([i,j])
     return pairs



def parametric_hopping(r1,r2,f):
  """ Generates a parametric hopping based on a function"""
  m = np.matrix([[0.0j for i in range(len(r2))] for j in range(len(r1))])
  for i in range(len(r1)):
    for j in range(len(r2)):
      m[i,j] = f(r1[i],r2[j]) # add hopping based on function
  return m


