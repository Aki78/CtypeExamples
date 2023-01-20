import ctypes
import numpy as np

# Load the shared library using ctypes
lib = ctypes.CDLL('./path/to/cfile.so')

# Define the function prototype for the C function
# void sum_arrays(double *result, double *a, double *b, int n)
lib.sum_arrays.argtypes = [np.ctypeslib.ndpointer(ctypes.c_double), 
                           np.ctypeslib.ndpointer(ctypes.c_double), 
                           np.ctypeslib.ndpointer(ctypes.c_double), 
                           ctypes.c_int]

# Input arrays
a = np.array([1, 2, 3], dtype=np.double)
b = np.array([4, 5, 6], dtype=np.double)

# Output array
result = np.zeros(3, dtype=np.double)

# Call the C function
n = len(a)
lib.sum_arrays(result, a, b, n)

print(result)
