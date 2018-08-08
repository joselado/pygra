# routines to call a function in parallel
from multiprocessing import Pool

def pcall(fun,args,cores=5):
  """Calls a function for every input in args"""
  p = Pool(cores) # create pool
  return p.map(fun,args) # return list



