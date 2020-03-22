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

## Band structure of graphene
```python
from pygra import geometry
g = geometry.honeycomb_lattice() # get the geometry object
h = g.get_hamiltonian() # get the Hamiltonian object
h.get_bands() # compute the band structure
```

## Mean field Hubbard model of a zigzag graphene ribbon
```python
from pygra import geometry
from pygra import scftypes
g = geometry.honeycomb_zigzag_ribbon(10) # create geometry of a zigzag ribbon
h = g.get_hamiltonian() # create hamiltonian of the system
mf = scftypes.guess(h,"ferro",fun=lambda r: [0.,0.,1.])
scf = scftypes.hubbardscf(h,nkp=30,filling=0.5,mf=mf)
h = scf.hamiltonian # get the Hamiltonian
h.get_bands(operator="sz") # calculate band structure
```

## Band structure of twisted bilayer graphene
```python
from pygra import specialgeometry
from pygra.specialhopping import twisted_matrix
g = specialgeometry.twisted_bilayer(3)
h = g.get_hamiltonian(mgenerator=twisted_matrix(ti=0.12))
h.get_bands(nk=100)
```

## Chern number of a quantum anomalous Hall insulator
```python
from pygra import geometry
from pygra import topology
g = geometry.honeycomb_lattice()
h = g.get_hamiltonian()
h.add_rashba(0.3) # Rashba spin-orbit coupling
h.add_zeeman([0.,0.,0.3]) # Zeeman field
c = topology.chern(h) # compute Chern number
print("Chern number is ",c)
```

## Band structure of a nodal line semimetal
```python
from pygra import geometry
from pygra import films
g = geometry.diamond_lattice_minimal()
g = films.geometry_film(g,nz=20)
h = g.get_hamiltonian()
h.get_bands()
```

## Surface spectral function of the Haldane model
```python
from pygra import geometry
from pygra import kdos
g = geometry.honeycomb_lattice()
h = g.get_hamiltonian()
h.add_haldane(0.05)
kdos.surface(h)
```

## Antiferromagnet-superconductor interface
```python
from pygra import geometry
g = geometry.honeycomb_zigzag_ribbon(10) # create geometry of a zigzag ribbon
h = g.get_hamiltonian(has_spin=True) # create hamiltonian of the system
h.add_antiferromagnetism(lambda r: (r[1]>0)*0.5) # add antiferromagnetism
h.add_swave(lambda r: (r[1]<0)*0.3) # add superconductivity
h.get_bands() # calculate band structure
```

## Fermi surface of a Kagome lattice
```python
from pygra import geometry
from pygra import spectrum
import numpy as np
g = geometry.kagome_lattice()
h = g.get_hamiltonian()
spectrum.multi_fermi_surface(h,nk=60,energies=np.linspace(-4,4,100),
        delta=0.1,nsuper=1)
```


# INSTALLATION #
Parts of the code are written in Fortran for a matter of performance.
To compile those functions you need to execute "install.sh" In case
they are not compiled, the library will still work but certain parts
will be substantially slower.

Parts of the code rely on Python libraries
 - numpy
 - scipy
 - multiprocess

