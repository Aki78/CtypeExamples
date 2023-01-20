import ctypes

# Load the .so library
my_lib = ctypes.CDLL('./path/to/library.so')

# Declare the function prototype
my_lib.add_numbers.argtypes = [ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double)]

# Input numbers as pointers
num1 = ctypes.c_double(1.5)
num2 = ctypes.c_double(2.5)
result = ctypes.c_double()

# Call the function
my_lib.add_numbers(ctypes.byref(num1), ctypes.byref(num2), ctypes.byref(result))

# Print the result
print(result.value)
