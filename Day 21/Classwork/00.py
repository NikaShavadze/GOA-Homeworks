"""
Given a non-empty array of integers, return the result of multiplying the values together in order. Example:
"""

def grow(arr):
    result = 1
    for i in arr:
        result *= i
    return result
        