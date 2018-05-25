# Reference to: https://www.quantstart.com/articles/LU-Decomposition-in-Python-and-NumPy
import pprint
import scipy
import scipy.linalg   # SciPy Linear Algebra Library
import numba

# Applying lu factorization with the "linalg" library function "lu" from scipy module.

A = scipy.array([ [7, 3, -1, 2], [3, 8, 1, -4], [-1, 1, 4, -1], [2, -4, -1, 6] ])

# @numba.njit (CANNOT)  
def factorize(A):
    P, L, U = scipy.linalg.lu(A)  # Numba is not able to jit this function in nopython mode
    return P,L,U

# @profile
def _(A):
    P,L,U = factorize(A)
    return P,L,U

_(A)
# print "A:"
# pprint.pprint(A)
#
# print "P:"
# pprint.pprint(P)
#
# print "L:"
# pprint.pprint(L)
#
# print "U:"
# pprint.pprint(U)
