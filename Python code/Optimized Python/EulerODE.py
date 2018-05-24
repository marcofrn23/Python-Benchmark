from __future__ import print_function, division
import cProfile
import numba
import math
from time import clock
import os
import numpy as np
import matplotlib.pyplot as plt

# Some nice environment variables
os.environ['NUMBA_WARNINGS']='1'
# os.environ['NUMBA_DEBUG_TYPEINFER']='1'    # Information abount types inferences
# os.environ['NUMBA_DEBUG_ARRAY_OPT']='1'    # Parallel computing information
# os.environ['NUMBA_NUM_THREADS']='1'        # Threading control
# os.environ['NUMBA_DUMP_ASSEMBLY']='1'      # Outputs the correspondant assembly code

# @profile
@numba.jit('float64(float64, float64)', nopython = True)#, parallel = True)
def func(t, x):
    return 3*(2**t) + t**2 +4*x    # First order ODE: x'(t) = func(t, x(t))

# @profile
@numba.jit('float64[:](float64, float64, float64, int64)', nopython = True)#, parallel = True)
def solve(x0, t0, T, N):
    dt = (T-t0)/float(N)
    time = np.arange(t0, T, dt)    # create mesh
    sol = np.zeros((N,))
    sol[0] = x0
    mid = dt/2.0
    for i in range(1, len(time)):
        tau = time[i-1]
        sol[i] = sol[i-1] + func(tau, sol[i-1])*dt
    return sol

# @profile
def euler():
    x0, t0 = 1,0   # Set Initial values
    T = 20
    N = 200
    time = np.arange(t0, T, (T-t0)/float(N))
    result = solve(x0,t0,T,N)
    return result



sol = euler()
# cProfile.run('solve(1,0,20,300)')

# plt.figure()
# plt.xlabel('time')
# plt.ylabel('x(t)')
# plt.plot(time1, sol, label = 'Runge-Kutta 4', color = 'g')
# plt.grid(True)
# plt.show()
