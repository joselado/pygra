from __future__ import print_function, division
import numpy as np

def cnpot(n=4,k=0.0,v=1.0,angle=0.):
  """Returns a function that generates a potential
  with C_n symmetry"""
  if n%2==0: f = np.cos # even 
  if n%2==1: f = np.sin # even 
  def fun(x0,y0,z=0.):
    """Function with the potential"""
    acu = 0. # result
    for i in range(n):
      x = np.cos(angle)*x0 + np.sin(angle)*y0
      y = np.cos(angle)*y0 - np.sin(angle)*x0
      arg = np.cos(i*np.pi*2/n)*x+np.sin(i*np.pi*2/n)*y
      acu += f(k*arg) 
    return v*acu/n
  return fun


