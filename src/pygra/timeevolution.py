import numpy as np
import scipy.linalg as lg
from . import algebra
from .ldos import spatial_dos,write_ldos
import os
from . import parallel

def evolve_local_state(h,i=0,ts=np.linspace(0.,20.,300)):
    """Evolve a state that is originally localized in a point"""
    if h.dimensionality!=0: raise # only for 0d
    # create the vector
#    v0 = np.zeros(h.intra.shape[0]) # zero dimensional
    if h.has_spin: raise
#    if h.has_spin: 
#        v0[2*i] = 1./np.sqrt(2)
#        v0[2*i+1] = 1./np.sqrt(2)
#    else: v0[i] = 1.0
#    if h.has_eh: 
#        v0[4*i] = 1./np.sqrt(2)
#        v0[4*i+1] = 1./np.sqrt(2)
    # now do the time evolution
#    (es,vs) = algebra.eigh(h.intra.real)
#    vs = vs.T # eigenvectors
#    ef = 6.0
#    vs = vs[es<ef,:] # get the eigenvectors
#    es = es[es<ef]
#    ws = np.array([np.conjugate(v0).dot(iv) for iv in vs]) # weights
    # do the tiem evolution
    from .chi import chargechi_row
    emin = np.min(algebra.eigvalsh(h.intra))
    es = np.linspace(emin,0.,int(max(ts)*2))
    cs = chargechi_row(h,es=es,i=i,delta=abs(emin)/len(es))
#    cs = np.array(cs).T
    def evol(t):
        out = np.array([c@np.exp(1j*es*t) for c in cs])
        return np.abs(out)
#        return np.abs(np.array(lg.expm(1j*h.intra*t))@v)**2
#        phi = np.exp(1j*es*t) # complex phases
#        out2 = np.array([iw*iv*iphi for (iw,iv,iphi) in zip(ws,vs,phi)])
#        print(out.shape)
#        out = np.zeros(v0.shape[0]) 
#        out += np.abs(np.sum(out2,axis=0))**2 # sum over eigenvectors
#        print(out.shape)
#        return out
    g = h.geometry
    os.system("rm -rf MULTITIMEEVOLUTION") # remove folder
    os.system("mkdir MULTITIMEEVOLUTION") # create folder
    fo = open("MULTITIMEEVOLUTION/MULTITIMEEVOLUTION.TXT","w")
    for t in ts: # loop over ts
        out = evol(t) # do the evolution
        out = spatial_dos(h,out) # resum if necessary
        name = "TIMEEVOLUTION_T_"+str(t)+"_.OUT" # name
        name2 = "MULTITIMEEVOLUTION/"+name # name
        write_ldos(g.x,g.y,out,output_file=name2) # write the LDOS
        fo.write(name+"\n") # write this file
    fo.close()






