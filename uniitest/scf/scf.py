import unittest
import numpy as np
import sys
sys.path.append("../../src/") # add the library
from pygra import geometry
from pygra import scftypes

error = 1e-2 # acceptable accuracy

class TestDMRG(unittest.TestCase):
    def test_NC(self):
        g = geometry.square_lattice()
        h = g.get_hamiltonian()
        mf = scftypes.guess(h,mode="antiferro",fun=0.0001)
        scf0 = scftypes.selfconsistency(h,mf=mf,nkp=5,filling=0.5,
                mode="Hubbard",silent=True)
        scf1 = scftypes.selfconsistency(h,mf=mf,nkp=5,filling=0.5,
                mode="Hubbard collinear",silent=True)
        passed = scf0.total_energy - scf1.total_energy
        passed = abs(passed)<error
        self.assertTrue(passed)

if __name__ == '__main__':
    unittest.main()
