# Python Benchmark

Project for "Computer architectures and networks" held by Prof. A. Mancini at UNIVPM.

The aim is to test and highly improve Python code performances to compare them with C++ ones.
To achieve this it will be used the just-in-time compilation function provided with the ***Numba*** Python module. Other features such as parallelization for multi-core execution will be tried out.

*"Numba gives you the power to speed up your applications with high performance functions written directly in Python. With a few annotations, array-oriented and math-heavy Python code can be just-in-time compiled to native machine instructions, similar in performance to C, C++ and Fortran, without having to switch languages or Python interpreters."*

For this Project I will use some important numerical calculus algorithm, such as methods for solving ODEs and matrices factorizations. Note that methods for these mathematical problems already exist in the Scipy module, which provides the best perfomances along with great ease of use. The aim here is only to test the Numba's features and to check its potential over popular and understandable numerical algorithms. 

Numba is supported by Anaconda and it is integrated in the **Python scientific stack**. For more detailed information about the Numba module, head to the [Official Documentation](https://numba.pydata.org/).

In this project I will also use **NumPy**, **cProfile**, **line_profiler**.

## Installing
### Numba:
GIT:
```
git clone git://github.com/numba/numba.git
```
Anaconda:
```
$ conda install numba
```
### line_profile:
```
$ pip install line_profiler
```
In order to run Python code in line-profiling mode, run via terminal:
```
$ kernprof -l -v codetoexecute.py
```
## Dependencies
- LLVM
- NumPy (version 1.9 or higher)


