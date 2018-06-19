# Python Benchmark

***Is it true that Python cannot compete with C++ performaces?***
___

The aim is to test and highly improve Python code performances to compare them with C++ ones.
To achieve this it has been used the just-in-time compilation function provided with the ***Numba*** Python module. 

*"Numba gives you the power to speed up your applications with high performance functions written directly in Python. With a few annotations, array-oriented and math-heavy Python code can be just-in-time compiled to native machine instructions, similar in performance to C, C++ and Fortran, without having to switch languages or Python interpreters."*

For this Project I have used some important numerical calculus algorithm, such as methods for solving ODEs and matrices factorizations. Note that methods for these mathematical problems already exist in the Scipy module, which provides the best perfomances along with great ease of use. The aim here is in fact only to test Numba's features sufficiently accurately to check its potential over popular and understandable numerical algorithms. More complex and fancy examples are findable via Internet.

Numba is supported by Anaconda and it is integrated in the **Python scientific stack**. For more detailed information about the Numba module, head to the [Official Documentation](https://numba.pydata.org/).

In this project I will also use **NumPy**, **cProfile**, **line_profiler**. For the final project report, click [here](https://github.com/marcofrn23/Python-Benchmark/blob/master/doc.pdf).

Benchmarks were carried out on a 2,7 GHz Intel Core i5® dual-core 8 GB Ram machine. Outcomes could vary across different architectures.

## Installing
### Numba:
GIT:
```
$ git clone git://github.com/numba/numba.git
```
Anaconda:
```
$ conda install numba
```
### line_profiler:
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
___

***Project for "Computer architectures and networks" held by Prof. A. Mancini at UNIVPM, Italy***
