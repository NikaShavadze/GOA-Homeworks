"""
Given an array of integers your solution should find the smallest integer.
"""
# 1


def find_smallest_int(arr):
    return min(arr)

# 2nd way


def find_smallest_int(arr):
    min_number = arr[0]
    for i in arr:
        if min_number > i:
            min_number = i
    return min_number
