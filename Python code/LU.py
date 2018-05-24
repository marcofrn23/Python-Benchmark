# Reference to http://quantstart.com/articles/LU-Decomposition-in-Python-and-NumPy.
# I have taken the code for LU fact. from here then I modified it to work with NumPy arrays
from __future__ import print_function, division
from pprint import pprint
import numba

def dot_numpy(A,B):  # Pythonic implementation of matrices multiplication
    return A@B

def dot_py(A,B):  # Unpythonic implementation of matrices multiplication
    L = len(A)
    C = np.identity(L)
    for i in range(L):
        for j in range(L):
            for k in range(L):
                C[i,j] += A[i,k]*B[k,j]
    return C

def pivot_matrix(m):
    n = len(m)

    ID = np.identity(n)
   
    for j in range(n):
        row = max(range(j, n), key=lambda i: abs(m[i][j]))  # Computes the row exchanges in the Gaussian elimination
        if j != row:
            ID[[j,row],:] = ID[[row,j],:] # swapping
    return ID

def lu(A):
    n = len(A)
    
    L = np.identity(n)  # Initialization of empty L & U matrices
    U = np.identity(n)

    P = pivot_matrix(A) # P is the Pivoting Matrix (PA = LU)
    A2 = dot_py(P,A)
    # A2 = dot_numpy(P,A)

    for j in range(n):
        for i in range(j+1):
            s1 = sum(U[k][j] * L[i][k] for k in range(i))
            U[i][j] = A2[i][j] - s1
        for i in range(j, n):
            s2 = sum(U[k][j] * L[i][k] for k in range(j))
            L[i][j] = (A2[i][j] - s2) / U[j][j]
    return (L, U, P)

A = np.array([[1.,3.,5.,9.,2.],
[4.,0.,9.,-7.,-8.],
[-4.,-3.,9.,-1.,5.]])
# A = [[1,3,5],[4,0,9],[-4,-3,9]] test
# pprint (lu(A))
