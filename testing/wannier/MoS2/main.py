import wannier


h = wannier.read_hamiltonian() # read the hamiltonian
h.write()
kpath = wannier.get_klist()
h.get_bands(kpath=kpath)
