"""
Given an array of integers, return a new array with each value doubled.
"""


def maps(a):
    new_list = []
    for i in a:
        i = i * 2
        new_list.append(i)
    return new_list
