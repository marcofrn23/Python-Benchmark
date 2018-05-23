from time import clock
from __future__ import print_function, division
import cProfile
import timeit

# def wrapper(func, *args):  # needed to use timeit with calls to functions with args
#     def wrapped():
#         return func(*args)
#     return wrapped

def timer(func, *args):
	t0 = clock()
	result, time = func(*args)
	elapsed = clock()-t0
	return elapsed, result, time

def test(calls, func, *args):
        if isinstance(n, int):
            times = [timer(func, *args)[0] for _ in range(n)]
        else:
            times = []
            while sum(times) < n:
                times.append(timer(func, *args)[0])
        print ('TIMES:\n', times)
        return times

# tosolve = lambda t, x: 3*(2**t) + t**2 +4*x
calls = 10
# result = test(calls, tosolve, 1,0,20,300)  # 'solve' here is intended as a function that solves an ODE
# print ('Fastest: ', min(result))
# print ('Slowest: ', max(result))
# print ('** Average **: ', sum(result)/len(result))
# print ('Number of calls: ', calls)

# cProfile.run('solve(*args)') # function profiling, run works like an "eval"

# wrapped = wrapper(solve, 1,0,20,300) # Instruction profiling, less accurate
# res = timeit(wrapped)
