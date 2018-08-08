import numpy.linalg as lg
from scipy.optimize import minimize_scalar
import numpy as np
import scipy.sparse.linalg as lgs
from scipy.sparse import csc_matrix

def minimize_gap(f):
  """Miimizes teh gp of the system, the argument is between 0 and 1"""
  return f(minimize_scalar(f,method="Bounded",bounds=(0.,1.),tol=0.0001).x)





def gap_line(h,kpgen):
  """Return a function with argument between 0,1, which returns the gap"""
  hk_gen = h.get_hk_gen() # get hamiltonian generator
  def f(k):
    kp = kpgen(k) # get kpoint
    hk = hk_gen(kp) # generate hamiltonian
#    es,ew = lgs.eigsh(csc_matrix(hk),k=4,which="LM",sigma=0.0)
    es = lg.eigvalsh(hk) # get eigenvalues
    g = np.min(es[es>0.]) - np.max(es[es<0.])
    return g  # return gap
  return f  # return gap
