# library to write in file the different states
import scipy.linalg as lg
import numpy as np
from ldos import spatial_dos as spatial_wave
from ldos import write_ldos as write_wave

def states0d(h,ewindow=[-.5,.5],signed=False):
  """Write in files the different states"""
  if not h.dimensionality==0: raise
  (evals,evecs) = lg.eigh(h.intra)
  evecs = evecs.transpose() # transpose list
  for i in range(len(evals)):
    if ewindow[0]<evals[i]<ewindow[1]: # if in the interval
      den = np.abs(evecs[i])**2
      den = spatial_wave(h,den) # resum if other degrees of freedom
      name="WAVE_"+str(i)+"_energy_"+str(evals[i])+".OUT"
      write_wave(h.geometry.x,h.geometry.y,den,output_file=name)
      if signed: # if you want to write signed waves
        v = evecs[i]
        ii = np.sum(v.imag)
        if ii<0.00001:
          den = spatial_wave(h,v.real) # resum if other degrees of freedom   
          name="WAVE_SIGNED_"+str(i)+"_energy_"+str(evals[i])+".OUT"
          write_wave(h.geometry.x,h.geometry.y,den,output_file=name)
        else:
          print "Warning, non real function"
