# generates diffeent types of klist

import numpy as np

def default(g,nk=400):
  """ Input is geometry"""
  if g.dimensionality == 2:
    b1 = np.array([1.,0.])
    b2 = np.array([0.,1.])
#    b2 = np.array([.5,np.sqrt(3)/2])
#    b2 = np.array([0.,-1.])
    fk = open("klist.in","w")  
    fk.write(str(nk)+"\n") # number of kpoints
    k = np.array([0.,0.]) # old kpoint
    kout= []
    for i in range(nk):
      k += (b1+b2) /(nk) # move kpoint 
      fk.write(str(k[0])+"   "+str(k[1])+"\n    ")
      kout.append(k) # store in array
    fk.close()
    # write bandlines
    fbl = open("BANDLINES.OUT","w")
    fbl.write("0   \Gamma\n")
    fbl.write(str(nk/3)+"   K\n")
    fbl.write(str(nk/2)+"   M\n")
    fbl.write(str(2*nk/3)+"   K'\n")
    fbl.write(str(nk)+"   \Gamma\n")
    fbl.close()
    return kout






def gen_default(k):
  """ Return a function which generates the path"""
  b1 = np.array([1.,0.])
  b2 = np.array([0.,1.])
  return k*(b1+b2) # return kpoint 




def kx(g,nk=400):
  """ Input is geometry"""
  if g.dimensionality == 2:
    b1 = np.array([1.,0.])
    b2 = np.array([0.,1.])
    fk = open("klist.in","w")  
    fk.write(str(nk)+"\n") # number of kpoints
    k = -b1/2 # old kpoint
    kout= []
    for i in range(nk):
      k += (b1) /(nk) # move kpoint 
      fk.write(str(k[0])+"   "+str(k[1])+"\n    ")
      kout.append(k) # store in array
    fk.close()
    # write bandlines
    fbl = open("BANDLINES.OUT","w")
    fbl.write("0   X_1\n")
    fbl.write(str(nk/2)+"   \Gamma\n")
    fbl.write(str(nk)+"   X_1\n")
    fbl.close()



