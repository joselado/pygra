# library to deal with the spectral properties of the hamiltonian
import numpy as np
import scipy.linalg as lg
import scipy.sparse.linalg as slg
import os
from .. import filesystem as fs

def poor_man_qpi(h,reciprocal=True,nk=20,energies=np.linspace(-3.0,3.0,80),
        output_folder="MULTIFERMISURFACE",**kwargs):
    """Compute the QPI using a poor-mans convolution of the k-DOS"""
    from ..fermisurface import fermi_surface_generator
    if reciprocal: fR = h.geometry.get_k2K_generator() # get matrix
    else:  fR = lambda x: x # get identity
    qs0 = h.geometry.get_kmesh(nk=20,nsuper=2)
    qs0 = qs0 - np.mean(qs0,axis=0)
    qs = np.array([fR(q) for q in qs0]) # convert
    es,ks,ds = fermi_surface_generator(h,reciprocal=False,info=False,
            energies=energies,
            nsuper=1,nk=nk,**kwargs)
    # we now have the energies, k-points and DOS, lets do a convolution
    fs.rmdir(output_folder) # remove folder
    fs.mkdir(output_folder) # create folder
    kdos = [poor_man_qpi_single_energy(ks,ds[:,i],qs) for i in range(len(es))]
    kdos = np.array(kdos).T # convert to array
    fo = open(output_folder+"/"+output_folder+".TXT","w")
    for i in range(len(es)): # loop over energies
        filename = output_folder+"_"+str(es[i])+"_.OUT" # name
        name = output_folder+"/"+filename
        np.savetxt(name,np.array([qs0[:,0],qs0[:,1],kdos[:,i]]).T)
        fo.write(filename+"\n")
        name = output_folder+"/DOS.OUT"
    name = "DOS.OUT"
    np.savetxt(name,np.array([es,np.sum(kdos,axis=0)]).T)
    fo.close()



def poor_man_qpi_single_energy(ks,ds,qs):
    """Do the convolution of the Fermi surfaces"""
#    return ds
    from ..interpolation import interpolator2d
    f0 = interpolator2d(ks[:,0],ks[:,1],ds) # interpolated k-DOS
    def f(k):
        """Define a periodic function"""
        k = k[:,0:2]%1.
        o = f0(k)
        return o
#    return f(qs)
    print("Doing")
    out = [np.mean(np.sqrt(f(ks)*f(ks+q))) for q in qs]
    return np.array(out) # return output




