#The link for the kyu : https://www.codewars.com/kata/56ff6a70e1a63ccdfa0001b1/train/python
import numpy as np

def array_madness(a, b):
    a = np.array(a)
    b = np.array(b)
    
    # Calculate sum of squares of array a and sum of cubes of array b
    sum_of_squares_a = np.sum(np.power(a, 2))
    sum_of_cubes_b = np.sum(np.power(b, 3))
    
    # Return True if the sum of squares of a is strictly greater than the sum of cubes of b
    return sum_of_squares_a > sum_of_cubes_b
