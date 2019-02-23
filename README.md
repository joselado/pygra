# AIM #
This is a Python library to compute tight binding models in different
dimensionalities and based on a variety of different lattices.

# CAPABILITIES #
- 0d, 1d, 2d and 3d systems
- Band structures
- Density of states
- Include magnetism, spin-orbit coupling and superconductivity
- Selfconsistent mean field calculations
- Topological characterization of electronic structures
- Green's function formalism for semi-infinite systems
- Spectral functions
- Kernel polynomial techniques
- Quantum Transport

# EXAMPLES #
In the examples folder there are several examples of usage of the
library. You will find among others:
- Quantum anomalous Hall and topological insulators
- Topological superconductors and Shiba lattices
- Magnetism in graphene materials
- Twisted bilayer graphene
- Nodal line semimetals 

# INSTALLATION #
Parts of the code are written in Fortran for a matter of performance.
To compile those functions you need to execute "install.sh" In case
they are not compiled, the library will still work but certain parts
will be substantially slower.

Parts of the code rely on Python libraries
 - numpy
 - scipy
 - multiprocess

