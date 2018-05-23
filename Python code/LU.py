# Reference to http://quantstart.com/articles/LU-Decomposition-in-Python-and-NumPy
from __future__ import print_function, division
import cProfile
from pprint import pprint
import numba

def mult_matrix(A, B):
    # With zip() the matrix B is transformed into a tuple of columns, with list() into an array
    unpB = list(zip(*B))
    return [[sum(_a*_b for _a,_b in zip(rowa,colb)) for colb in unpB] for rowa in A]

def pivot_matrix(m):
    """Creates the pivoting matrix for m (P)."""
    # Compute the pivoting matrix that represent row exchanges in Gaussian elimination
    n = len(m)
    # Creates an identity matrix with float values
    ID = [[float(i == j) for i in range(n)] for j in range(n)]
    # swaps by comparing max values of each row
    for j in range(n):
        row = max(range(j, n), key=lambda i: abs(m[i][j]))
        if j != row:
            ID[j], ID[row] = ID[row], ID[j] # swapping 
    return ID

def lu(A):
    """Decomposes a nxn matrix A by PA=LU and returns L, U and P.
    A must be square."""
    n = len(A)
    # Initialization of empty L & U matrices
    L = [[0.0] * n for i in range(n)]
    U = [[0.0] * n for i in range(n)]

    P = pivot_matrix(A)
    A2 = mult_matrix(P, A)

    for j in range(n):
        L[j][j] = 1.0
        for i in range(j+1):
            s1 = sum(U[k][j] * L[i][k] for k in range(i))
            U[i][j] = A2[i][j] - s1
        for i in range(j, n):
            s2 = sum(U[k][j] * L[i][k] for k in range(j))
            L[i][j] = (A2[i][j] - s2) / U[j][j]
    return (L, U, P)

# A = [[1,3,5],[4,0,9],[-4,-3,9]] test
# print (lu(A))
