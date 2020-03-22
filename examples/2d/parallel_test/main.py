# Add the root path of the pygra library
import os ; import sys ; sys.path.append(os.environ['PYGRAROOT'])

from pygra importgeometry
import topology
import klist
#for i in range(3):
g = geometry.honeycomb_lattice()
g = g.supercell(3)
h = g.get_hamiltonian(has_spin=True)
import time
import parallel
t0 = time.perf_counter()
parallel.cores = 1 # run in 1 core
h.get_dos(nk=10,use_kpm=False)
t1 = time.perf_counter()
print("Time in parallel",t1-t0)
exit()
parallel.cores = 1 # run in 1 core
h.get_dos(nk=10,use_kpm=False)
t2 = time.perf_counter()
print("Time in serial",t2-t1)
#dos.dos(h,nk=100,use_kpm=True)
