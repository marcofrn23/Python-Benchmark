import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import numba
import time

# Solving ODEs with odeint function from the scipy module. Code is obviously shorter, but it is much slower than 
# in 'RungeKuttaODE-opt.py' even with the addition of the njit decorator to the function that evals the equation

@numba.njit
def func(x,t):
    return t**2 - 5*x

# initial condition
y0 = 5
t0 = 0

# Time interval and steps
T = 20
N = 200
dt = (T-t0)/float(N)


# time points
t = np.linspace(t0,T,dt)

# solve ODE
def integrate(func, y0, t):
    return odeint(func,y0,t)

y = integrate(func, y0, t)

# plot results
# plt.plot(t,y)
# plt.xlabel('time')
# plt.ylabel('y(t)')
# plt.show()
