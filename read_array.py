import ctypes
import numpy as np

# Manually load the missing DLL first
ctypes.CDLL(r"C:\msys64\ucrt64\bin\libstdc++-6.dll")

# Load the shared library
lib = ctypes.windll.LoadLibrary(r"H:\Work\checkcodes\prj\array_lib.dll")  # Use 'array_lib.dll' on Windows

# Set the return type to a pointer to an 8x8 double array
lib.getarr.restype = ctypes.POINTER(ctypes.c_int * 16 * 1)

# Get the array from C++
ptr = lib.getarr()

# Convert to a NumPy array for easier visualization
matrix = np.ctypeslib.as_array(ptr, shape=(8, 8))
matrix2= np.abs(matrix[:,:])

# Print the matrix with 2 decimal places
#np.set_printoptions(round=matrix)  # Suppress scientific notation
print("Python Retrieved Matrix:")
print(matrix2)
