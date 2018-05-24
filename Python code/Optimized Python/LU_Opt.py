from __future__ import print_function, division
import cProfile
from pprint import pprint
import numba
import time
import os
import numpy as np

# Some nice environment variables
os.environ['NUMBA_WARNINGS']='1'
# os.environ['NUMBA_DEBUG_TYPEINFER']='1'    # Information abount types inferences
# os.environ['NUMBA_DEBUG_ARRAY_OPT']='1'    # Parallel computing information
# os.environ['NUMBA_NUM_THREADS']='1'        # Threading control 
# os.environ['NUMBA_DUMP_ASSEMBLY']='1'      # Outputs the correspondant assembly code 

# @numba.jit('float64[:,:](float64[:,:], float64[:,:])',nopython = True)
# def dot_numpy(A, B):
#     return np.dot(A,B)

@numba.jit('float64[:,:](float64[:,:], float64[:,:])', nopython = True, nogil = True) #,parallel = True)
def dot_py(A,B):
    L = len(A)
    C = np.identity(L)
    for i in range(L):
        for j in range(L):
            for k in range(L):
                C[i,j] += A[i,k]*B[k,j]
    return C


# @numba.jit('float64[:][:](float64[:][:])', nopython = True) # Not necessary
def pivot_matrix(m):
    """Creates the pivoting matrix for m (P)."""
    # Compute the pivoting matrix that represent row exchanges in Gaussian elimination
    n = len(m)
    # Creates an identity matrix with float values
    ID = np.identity(n)
    # swaps by comparing max values of each row
    for j in range(n):
        row = max(range(j, n), key=lambda i: abs(m[i][j]))
        if j != row:
            ID[[j,row],:] = ID[[row,j],:] # swapping
    return ID


# @profile  # line_profiler decorator, the below function will be profiled
def lu(A):
    n = len(A)
    # Initialization of empty L & U matrices
    L = np.identity(n)
    U = np.identity(n)

    P = pivot_matrix(A)
    A2 = dot_py(P,A)
    # A2 = dot_numpy(P,A)

    for j in range(n):
        L[j][j] = 1.0
        for i in range(j+1):
            s1 = sum(U[k][j] * L[i][k] for k in range(i))
            U[i][j] = A2[i][j] - s1
        for i in range(j, n):
            s2 = sum(U[k][j] * L[i][k] for k in range(j))
            L[i][j] = (A2[i][j] - s2) / U[j][j]
    return (L, U, P)

A = np.random.random((5,5))

# Searching for bottlenecks
cProfile.run('lu(A)')
# Line Profiling: run via terminal $ kernprof -l -v Lu.py


L,U,P = lu(A)
#pprint(L,U)
