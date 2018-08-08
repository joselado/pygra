# compile the fortran routine
f2py -llapack -c -m gauss_inv gauss_inv.f90

