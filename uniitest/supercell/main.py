import unittest
import numpy as np
import sys
sys.path.append("../../src/") # add the library
from pygra import geometry
from pygra import scftypes

error = 1e-7 # acceptable accuracy

def geth(n1,n2,g0):
    g = g0.supercell(n1)
    h = g.get_hamiltonian()
    h.add_rashba(0.2)
    h.add_zeeman([0.,0.2,0.])
    h = h.supercell(n2)
    return h



class Test(unittest.TestCase):
    def test_1(self):
        g = geometry.honeycomb_lattice()
        g = g.supercell(2)
        k = np.random.random(3)
        h1 = geth(3,1,g).get_hk_gen()(k)
        h2 = geth(1,3,g).get_hk_gen()(k)
        diff = np.max(np.abs(h1-h2))
        print("Error = ",diff)
        passed = diff<error
        self.assertTrue(passed)

if __name__ == '__main__':
    unittest.main()
