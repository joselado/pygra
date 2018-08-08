def find_first_neighbor(x1,y1,x2,y2):
   """Calls the fortran routine"""
   import neighbor_fortran as nf
   (npairs,pairs) = nf.find_first_neighbor(x1,y1,x2,y2)
   # retain only the first npairs elements
   pairs = [pairs[i] for i in range(npairs)]
   return pairs # return the pairs


