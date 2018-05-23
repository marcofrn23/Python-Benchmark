from __future__ import print_function, division
import cProfile
import numba
import numpy as np
import matplotlib.pyplot as plt

def func(t, x):
    return 3*(t) +5*x  # choose an equation here


def solve(x0, t0, T, N):
    dt = (T-t0)/float(N)
    time = np.arange(t0, T, dt)    # create mesh
    sol = np.zeros((N,))
    sol[0] = x0
    mid = dt/2.0
    for i in range(1, len(time)):
        tau = time[i-1]
        sol[i] = sol[i-1] + func(tau, sol[i-1])*dt
    return sol, time

sol, time = solve(3,0,10,30) # choose initial values and step here

# plt.figure()
# plt.xlabel('time')
# plt.ylabel('x(t)')
# plt.plot(time, sol, label = 'Euler', color = 'g')
# plt.grid(True)
# plt.show()
