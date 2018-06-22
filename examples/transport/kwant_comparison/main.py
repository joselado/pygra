
import sys
sys.path.append("../../../pygra")  # add pygra library

import disorder
import geometry
import heterostructures
import numpy as np
import matplotlib.pyplot as plt

g = geometry.square_ribbon(1)
h = g.get_hamiltonian()
#h.add_peierls(.2)
h.remove_spin()
hr = h.copy()
hl = h.copy()

hr.shift_fermi(.4)
hl.shift_fermi(.7)


hcs = [h] + [disorder.phase(h,w=0.5) for i in range(10)] +[h]
ht1 = heterostructures.create_leads_and_central_list(hr,hl,hcs)
ht2 = ht1.copy()
#ht2 = ht2.block2full()


ht2.didv(0.0,kwant=True)
#exit()



es = np.linspace(0.,1,30)
ts1 = np.array([ht1.didv(e,delta=1e-11,kwant=False) for e in es])
ts2 = np.array([ht2.didv(e,delta=1e-11,kwant=True) for e in es])

print("Error",np.sum(np.abs(ts1-ts2)))
print(ts1)
print(ts2)
plt.scatter(es,ts1-ts2)
plt.show()


