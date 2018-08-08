def green_renormalization(intra,inter,energy=0.0,nite=None,
                            error=0.0001,info=False,delta=0.001):
  """ Calculates bulk and surface Green function by a renormalization
  algorithm, as described in I. Phys. F: Met. Phys. 15 (1985) 851-858 """

  e = np.matrix(np.identity(len(intra))) * (energy + 1j*delta)
  ite = 0
  alpha = inter
  beta = inter.H
  epsilon = intra
  epsilon_s = intra + inter * (e-intra).I * inter.H
  epsilon_s = intra
  while True: # implementation of Eq 11
    einv = (e - epsilon).I # inverse
    epsilon_s = epsilon_s + alpha * einv * beta
    epsilon = epsilon + alpha * einv * beta + beta * einv * alpha
    alpha = alpha * einv * alpha  # new alpha
    beta = beta * einv * beta  # new beta
    ite += 1
    # stop conditions
    if not nite == None:
      if ite > nite:  break
    else:
      if np.max(np.abs(alpha))<error and np.max(np.abs(beta))<error: break
  if info:
    print "Converged in ",ite,"iterations"
  g_surf = (e - epsilon_s).I # surface green function
  return g_surf

