# library for 2d crystals


class hamiltonian2d:
  """Class for a 2d hamiltonian"""
  o = 0.0
  t_xp = 0.0  # 1 0
  t_xm = 0.0  # -1 0
  t_yp = 0.0  # 0 1
  t_ym = 0.0  # 0 -1
  t_xp_xp = 0.0  # 1  1
  t_xm_ym = 0.0  # -1  -1
  t_xm_xp = 0.0  # -1  1
  t_xp_ym = 0.0  # 1  1



def ribbon2plane(h,n=4):
  """ Clculates a 2d hamiltonian from the ribbon"""
  h2d = hamiltonian2d() # create the object
  



