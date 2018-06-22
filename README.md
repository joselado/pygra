# AIM #
This is a Python library to compute tight binding models in different
dimensionalities and based on a variety of different lattices

# CAPABILITIES #
- Band structure calculation
- Density of states
- Include magnetism, spin-orbit coupling and superconductivity
- Selfconsistent mean field calculations
- Topological characterization of electronic structures
- Quantum Transport

# EXAMPLES #
In the examples folder there are several examples of usage of the
library

# INSTALATION #
Parts of the code are written in Fortran for a matter of performance.
To compile those functions you need to execute "install.sh" In case
they are not compiled, the library will still work but certain parts
will be substantially slower.

Parts of the library rely on common Python libraries such as
 - numpy
 - scipy

