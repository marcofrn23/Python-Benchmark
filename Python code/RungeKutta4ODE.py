from __future__ import print_function, division
import cProfile
import numba
import numpy as np
import matplotlib.pyplot as plt

def func(t, x):
    return 3*(2**t) + t**2 +4*x  # choose an equation here

def solve(x0, t0, T, N):
    dt = (T-t0)/float(N)
    time = np.arange(t0, T, dt)    # create mesh
    sol = np.zeros((N,))
    sol[0] = x0
    mid = dt/2.0
    
    for i in range(1, len(time)):
    
        tau = time[i-1]
        k1 = func(tau, sol[i-1])*dt
        k2 = func(tau+mid, sol[i-1]+k1/2)*dt
        k3 = func(tau+mid, sol[i-1]+k2/2)*dt
        k4 = func(tau+dt, sol[i-1]+k3)*dt
        
        sol[i] = sol[i-1] + (k1 + 2*k2 + 2*k3 + k4)/6
    return sol, time
    
sol, time = solve(0,1,10,200) # choose initial values and step here
# plt.figure()
# plt.xlabel('time')
# plt.ylabel('x(t)')
# plt.plot(time, sol, label = 'Runge-Kutta 4', color = 'g')
# plt.grid(True)
# plt.show()
